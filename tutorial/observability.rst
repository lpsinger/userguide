Basic Observability Calculations
================================

Now we are going to teach our GCN handler how to determine whether a
gravitational-wave event is observable. We are going to use the
:doc:`astropy.coordinates <astropy:coordinates/index>` module. (See also the
Astropy example on :doc:`observation planning in Python
<astropy:generated/examples/coordinates/plot_obs-planning>`.) First, we will
need to import a few extra Python modules::

    import astropy.coordinates
    import astropy.time
    import astropy.units as u

The LIGO/Virgo probability sky maps are always in equatorial coordinates. Once
we have looked up the coordinates of the HEALPix pixels, we will use Astropy to
transform those coordinates to a horizontal (altitude–azimuth) frame for a
particular site on the Earth at a particular time. Then we can quickly
determine which pixels are visible from that site at that time, and integrate
(sum) the probability contained in those pixels.

.. note::
   You may want to do something more sophisticated like determine how much of
   the probability is visible for at least a certain length of time. This
   example will illustrate one key function of HEALPix (looking up coordinates
   of the grid with :func:`hp.pix2ang <healpy.pixelfunc.pix2ang>`) and some of
   the key positional astronomy functions with Astropy. For more advanced
   functionality, we recommend the astroplan_ package.

::

    def prob_observable(m, header):
        """
        Determine the integrated probability contained in a gravitational-wave
        sky map that is observable from a particular ground-based site at a
        particular time.

        Bonus: make a plot of probability versus UTC time!
        """

        # Determine resolution of sky map
        npix = len(m)
        nside = hp.npix2nside(npix)

        # Get time now
        time = astropy.time.Time.now()
        # Or at the time of the gravitational-wave event...
        # time = astropy.time.Time(header['MJD-OBS'], format='mjd')
        # Or at a particular time...
        # time = astropy.time.Time('2015-03-01 13:55:27')

        # Geodetic coordinates of observatory (example here: Mount Wilson)
        observatory = astropy.coordinates.EarthLocation(
            lat=34.2247*u.deg, lon=-118.0572*u.deg, height=1742*u.m)

        # Alt/az reference frame at observatory, now
        frame = astropy.coordinates.AltAz(obstime=time, location=observatory)

        # Look up (celestial) spherical polar coordinates of HEALPix grid.
        theta, phi = hp.pix2ang(nside, np.arange(npix))
        # Convert to RA, Dec.
        radecs = astropy.coordinates.SkyCoord(
            ra=phi*u.rad, dec=(0.5*np.pi - theta)*u.rad)

        # Transform grid to alt/az coordinates at observatory, now
        altaz = radecs.transform_to(frame)

        # Where is the sun, now?
        sun_altaz = astropy.coordinates.get_sun(time).transform_to(altaz)

        # How likely is it that the (true, unknown) location of the source
        # is within the area that is visible, now? Demand that sun is at
        # least 18 degrees below the horizon and that the airmass
        # (secant of zenith angle approximation) is at most 2.5.
        prob = m[(sun_altaz.alt <= -18*u.deg) & (altaz.secz <= 2.5)].sum()

        # Done!
        return prob

Finally, we need to update our GCN handler to call this function::

    @gcn.handlers.include_notice_types(
        gcn.notice_types.LVC_PRELIMINARY,
        gcn.notice_types.LVC_INITIAL,
        gcn.notice_types.LVC_UPDATE)
    def process_gcn(payload, root):
        # Respond only to 'test' events.
        # VERY IMPORTANT! Replce with the following line of code
        # to respond to only real 'observation' events.
        # if root.attrib['role'] != 'observation':
        #    return
        if root.attrib['role'] != 'test':
            return

        # Respond only to 'CBC' events. Change 'CBC' to "Burst'
        # to respond to only unmodeled burst events.
        if root.find(".//Param[@name='Group']").attrib['value'] != 'CBC':
            return

        skymap_url = root.find(".//Param[@name='skymap_fits']").attrib['value']

        skymap, header = hp.read_map(skymap_url, h=True, verbose=False)
        prob = prob_observable(skymap, header)
        print('Source has a {:d}% chance of being observable now'.format(
            int(round(100 * prob))))
        if prob > 0.5:
            pass # FIXME: perform some action

Let's run the new GCN handler now...

::

    # Listen for GCNs until the program is interrupted
    # (killed or interrupted with control-C).
    gcn.listen(handler=process_gcn)

When you run this script, each time you receive a sample LIGO/Virgo GCN Notice,
it will print something like the following (note that probability will change
as a function of time):

    Source has a 76% chance of being observable now

.. _astroplan: https://astroplan.readthedocs.io/
