from importlib import metadata

__version__ = metadata.version("dj_sentry")

default_app_config = "dj_sentry.apps.SentryConfig"
