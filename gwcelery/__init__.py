"""Celery application initialization."""

from celery import Celery
import pkg_resources

from .conf import playground

__all__ = ('app',)

__version__ = pkg_resources.get_distribution(__package__).version

# Use redis broker, because it supports locks (and thus singleton tasks).
app = Celery(__name__, broker='redis://', autofinalize=False)
"""Celery application object."""

# Register all tasks.
app.autodiscover_tasks([__name__])

# Add default configuration.
app.add_defaults(playground)
app.finalize()

# Customize configuration from environment variable.
app.config_from_envvar('CELERY_CONFIG_MODULE', silent=True)

# Use the same URL for both the result backend and the broker.
app.conf['result_backend'] = app.conf.broker_url
