"""Data quality and detector characterization tasks.

These tasks are mostly focused on checking interferometer state vectors. By
design, the [LIGO]_ and [Virgo]_ state vectors share the same definitions for
the first 8 fields.

LIGO also has a [DMT]_ DQ vector that provides some additional instrumental
checks.

References
----------
.. [LIGO] https://wiki.ligo.org/Calibration/TDCalibReview
.. [Virgo] https://dcc.ligo.org/G1801125/
.. [DMT] https://wiki.ligo.org/DetChar/DmtDqVector
"""
import glob

from celery.exceptions import Ignore
from celery.utils.log import get_task_logger
from glue.lal import Cache
from gwpy.timeseries import Bits, StateVector
import numpy as np

from ..celery import app
from . import gracedb

__author__ = 'Geoffrey Mo <geoffrey.mo@ligo.org>'

log = get_task_logger(__name__)

dmt_dq_vector_bits = Bits(
    channel='DMT-DQ_VECTOR',
    bits={
        1: 'NO_OMC_DCPD_ADC_OVERFLOW',
        2: 'NO_DMT-ETMY_ESD_DAC_OVERFLOW'
    },
    description={
        'NO_OMC_DCPD_ADC_OVERFLOW': 'OMC DCPC ADC not overflowing',
        'NO_DMT-ETMY_ESD_DAC_OVERFLOW': 'ETMY ESD DAC not overflowing'
    }
)
"""DMT DQ vector bits (LIGO only)."""


state_vector_bits = Bits(
    channel='GDS-CALIB_STATE_VECTOR or DQ_ANALYSIS_STATE_VECTOR',
    bits={
        0: 'HOFT_OK',
        1: 'OBSERVATION_INTENT',
        5: 'NO_STOCH_HW_INJ',
        6: 'NO_CBC_HW_INJ',
        7: 'NO_BURST_HW_INJ',
        8: 'NO_DETCHAR_HW_INJ'
    },
    description={
        'HOFT_OK': 'h(t) was successfully computed',
        'OBSERVATION_INTENT': '"observation intent" button is pushed',
        'NO_STOCH_HW_INJ': 'No stochastic HW injection',
        'NO_CBC_HW_INJ': 'No CBC HW injection',
        'NO_BURST_HW_INJ': 'No burst HW injection',
        'NO_DETCHAR_HW_INJ': 'No HW injections for detector characterization'
    }
)
"""State vector bitfield definitions for LIGO and Virgo."""


def create_cache(ifo):
    """Find .gwf files and create cache.

    Parameters
    ----------
    ifo : str
        Interferometer name (e.g. ``H1``).

    Returns
    -------
    :class:`glue.lal.Cache`

    Example
    -------
    >>> create_cache('H1')
    [<glue.lal.CacheEntry at 0x7fbae6b71278>,
      <glue.lal.CacheEntry at 0x7fbae6ae5b38>,
      <glue.lal.CacheEntry at 0x7fbae6ae5c50>,
     ...
      <glue.lal.CacheEntry at 0x7fbae6b15080>,
      <glue.lal.CacheEntry at 0x7fbae6b15828>]

    Note that running this example will return an I/O error, since /dev/shm
    gets overwritten every 300 seconds.

    Notes
    -----
    There are two main ways which this function can fail, which need to
    be accounted for in the future. The first is that the directory
    (typically /dev/shm/llhoft) is found, but the files in question
    corresponding to the timestamp are not in place. This can happen if the
    function is late to the game, and hence the data have been deleted from
    memory and are no longer stored in /dev/shm/llhoft. It can also happen if
    through some asynchronous processes, the call is early, and the data files
    have not yet been written to /dev/shm/llhoft. The second way is if
    /dev/shm/llhoft is not found and hence data never shows up.

    In these cases, the desired behaviour will be for the function to wait a
    period of ~5 seconds and try again. If it still returns an I/O error of
    this type, then the function will return a flag and stop trying (this can
    happen by setting a maximum number of retries to 1).

    This is important for if gwcelery is run locally (and not on a cluster),
    where /dev/shm is inaccessible.
    """
    pattern = app.conf['llhoft_glob'].format(detector=ifo)
    filenames = glob.glob(pattern)
    return Cache.from_urls(filenames)


def check_vector(cache, channel, start, end, bits, logic_type='all'):
    """Check timeseries of decimals against a bitmask.
    This is inclusive of the start time and exclusive of the end time, i.e.
    [start, ..., end).

    Parameters
    ----------
    cache : :class:`glue.lal.Cache`
        Cache from which to check.
    channel : str
        Channel to look at, e.g. ``H1:DMT-DQ_VECTOR``.
    start, end : int or float
        GPS start and end times desired.
    bits: :class:`gwpy.TimeSeries.Bits`
        Definitions of the bits in the channel.
    logic_type : str, optional
        Type of logic to apply for vetoing.
        If ``all``, then all samples in the window must pass the bitmask.
        If ``any``, then one or more samples in the window must pass.

    Returns
    -------
    dict
        Maps each bit in channel to its state.

    Example
    -------
    >>> check_vector(cache, 'H1:GDS-CALIB_STATE_VECTOR', 1216496260,
                     1216496262, state_vector_bits)
    {'H1:HOFT_OK': True,
     'H1:OBSERVATION_INTENT': True,
     'H1:NO_STOCH_HW_INJ': True,
     'H1:NO_CBC_HW_INJ': True,
     'H1:NO_BURST_HW_INJ': True,
     'H1:NO_DETCHAR_HW_INJ': True}
    """
    if logic_type not in ('any', 'all'):
        raise ValueError("logic_type must be either 'all' or 'any'.")
    bitname = '{}:{}'
    try:
        statevector = StateVector.read(cache, channel, start=start, end=end,
                                       bits=bits)
    except IndexError:
        # FIXME: figure out how to get access to low-latency frames outside
        # of the cluster. Until we figure that out, actual I/O errors have
        # to be non-fatal.
        log.exception('Failed to read from low-latency frame files')
        return {bitname.format(channel.split(':')[0], key):
                None for key in bits if key is not None}
    else:
        return {bitname.format(channel.split(':')[0], key):
                bool(getattr(np, logic_type)(getattr(value, 'value')))
                for key, value in statevector.get_bit_series().items()}


@app.task(shared=False)
def check_vectors(event, superevent_id, start, end):
    """Perform data quality checks for an event. This includes checking the DQ
    overflow vector (DMT-DQ_VECTOR) for LIGO and the first and second bits of
    the calibration state vectors for LIGO (GDS-CALIB_STATE_VECTOR) and Virgo
    (DQ_ANALYSIS_STATE_VECTOR), as well as the injection states for all three
    detectors.

    The results of these checks are logged into the superevent specified
    by ``superevent_id``, and ``DQOK``, ``DQV``, and ``INJ`` labels are
    appended as appropriate.

    This skips MDC events.

    Parameters
    ----------
    event : dict
        Details of event.
    superevent_id : str
        GraceID of event to which to log.
    start, end : int or float
        GPS start and end times desired.

    Returns
    -------
    event : dict
        Details of event.
    """
    # Skip MDC events.
    if event.get('search') == 'MDC':
        log.info('Skipping state vector checks because %s is an MDC',
                 event['graceid'])
        return event

    instruments = event['instruments'].split(',')
    pre, post = app.conf['check_vector_prepost'][event['pipeline']]
    start, end = start - pre, end + post

    ifos = {key.split(':')[0] for key, val in
            app.conf['llhoft_channels'].items()}
    caches = {ifo: create_cache(ifo) for ifo in ifos}
    states = {}
    for channel, bits in app.conf['llhoft_channels'].items():
        states.update(check_vector(caches[channel.split(':')[0]], channel,
                                   start, end, globals()[bits]))

    dq_states = {key: value for key, value in states.items()
                 if key.split('_')[-1] != 'INJ'}
    inj_states = {key: value for key, value in states.items()
                  if key.split('_')[-1] == 'INJ'}
    active_dq_states = {key: value for key, value in dq_states.items()
                        if key.split(':')[0] in instruments}
    active_inj_states = {key: value for key, value in inj_states.items()
                         if key.split(':')[0] in instruments}

    # Labeling INJ to GraceDb
    if False in active_inj_states.values():
        # Label 'INJ' if injection found in active IFOs
        gracedb.create_label('INJ', superevent_id)
    if False in inj_states.values():
        # Write all found injections into GraceDb log
        inj_fmt = ("Looking across all ifos, {} is False. No other HW"
                   " injections found.")
        inj_msg = inj_fmt.format(
            ', '.join(k for k, v in inj_states.items() if v is False))
        gracedb.client.writeLog(superevent_id, inj_msg,
                                tag_name=['data_quality'])
    elif all(inj_states.values()):
        gracedb.client.writeLog(superevent_id, 'No HW injections found.',
                                tag_name=['data_quality'])

    # Determining overall_dq_active_state
    if None in active_dq_states.values():
        overall_dq_active_state = None
    elif False in active_dq_states.values():
        overall_dq_active_state = False
    else:
        assert all(active_dq_states.values())
        overall_dq_active_state = True
    fmt = ("detector state for active instruments is {}."
           " For all instruments, bits good ({}), bad ({}), unknown({}).")
    msg = fmt.format(
        {None: 'unknown', False: 'bad', True: 'good'}[overall_dq_active_state],
        ', '.join(k for k, v in active_dq_states.items() if v is True),
        ', '.join(k for k, v in active_dq_states.items() if v is False),
        ', '.join(k for k, v in active_dq_states.items() if v is None),
    )
    # Labeling DQOK/DQV to GraceDb
    gracedb.client.writeLog(superevent_id, msg, tag_name=['data_quality'])
    if overall_dq_active_state is True:
        gracedb.create_label('DQOK', superevent_id)
    elif overall_dq_active_state is False:
        gracedb.create_label('DQV', superevent_id)
        # Halt further proessing of canvas
        raise Ignore('vetoed by state vector')

    return event
