import logging

from django.apps import AppConfig
from django.conf import settings

import pkg_resources
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

log = logging.getLogger(__name__)


class SentryConfig(AppConfig):
    name = "dj_sentry"
    label = "dj_sentry"
    verbose_name = "Django Sentry client"

    def ready(self):
        sentry_dsn = getattr(settings, "SENTRY_DSN", None)
        sentry_env = getattr(settings, "SENTRY_ENVIRONMENT", None)
        sentry_app_pkg = getattr(settings, "SENTRY_APP_PACKAGE_NAME", None)
        sentry_extra_integrations = getattr(settings, "SENTRY_EXTRA_INTEGRATIONS", [])
        sentry_extra_opts = getattr(settings, "SENTRY_EXTRA_OPTS", {})

        if sentry_dsn is None or sentry_env is None:
            raise ValueError(
                "Unable to configure Sentry client. Some mandatory settings are not set"
                " in the settings of the application."
            )

        current_release = None
        if sentry_app_pkg:
            current_release = pkg_resources.get_distribution(sentry_app_pkg).version

        if "traces_sample_rate" not in sentry_extra_opts:
            # Do not use by default the tracing system of Sentry.
            sentry_extra_opts["traces_sample_rate"] = 0

        if "send_default_pii" not in sentry_extra_opts:
            # Send by default user's information to Sentry
            sentry_extra_opts["send_default_pii"] = True

        # Initialize Sentry SDK
        sentry_sdk.init(
            dsn=sentry_dsn,
            environment=sentry_env,
            integrations=[DjangoIntegration(), *sentry_extra_integrations],
            release=current_release,
            **sentry_extra_opts,
        )

        log.info("Sentry client is configured!")
