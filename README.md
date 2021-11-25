# Dj_sentry

This Django application intialize [Sentry SDK](https://docs.sentry.io/platforms/python/) to your Django application.

## How to install

You can install this packaging by using:

```bash
pip install dj_sentry
```

Alternatively, if you use a package manager, for example Poetry, you can use:

```bash
poetry add dj_sentry
```

## How to configure

In your `settings`files, add the following settings to configure the Sentry SDK according with your needs:

| Setting                      | Type                | Description |
|------------------------------|---------------------|-------------|
| `SENTRY_DSN`                 | `str` **mandatory** | [Sentry project DSN](https://docs.sentry.io/product/sentry-basics/dsn-explainer/). |
| `SENTRY_ENVIRONMENT`         | `str` **mandatory** | Environment where the application is running (for example: *production*, *pre-production*, *staging*) |
| `SENTRY_APP_PACKAGE_NAME`    | `str` *optional*    | Package name of your application¹. |
| `SENTRY_EXTRA_INTEGRATIONS`  | `list` *optional*   | List of [Sentry integrations](https://docs.sentry.io/platforms/python/configuration/integrations/) you want to use (in addition of the Django integration already set-up)  |
| `SENTRY_EXTRA_OPTS`          | `dict` *optional*   | Dict with additionnal settings for configuring the Sentry client. See [Sentry client configuration](https://docs.sentry.io/platforms/python/configuration/) |

¹: We use [`pkg_resources`](https://setuptools.pypa.io/en/latest/pkg_resources.html) from Setuptools to get the package version of your application and send it on every events. This setting is optional but **highly** recommended.

By default, the setting [`traces_sample_rate`](https://docs.sentry.io/platforms/python/configuration/options/#traces-sample-rate) [`send_default_pii`](https://docs.sentry.io/platforms/python/configuration/options/#send-default-pii) have the following default values

| Setting                      | Value                                     |
|------------------------------|-------------------------------------------|
| `traces_sample_rate`         | `0` (no tracing samples sent to Sentry)   |
| `send_default_pii`           | `True` (send user information in events)  |

You can change de values of those settings by using the `SENTRY_EXTRA_OPTS` setting. For example, to disable the setting that send user informations:

```python
SENTRY_EXTRA_OPTS = {
    "send_default_pii": False,  # Do not send user information in Sentry events
}
```

Here's an example of valid configuration:

```python
from sentry_sdk.integrations.redis import RedisIntegration
from company_cms.utils.sentry import before_send_filter

# Your Django configuration ...

SENTRY_DSN = "https://<token>@sentry.company.com/<project_id>"
SENTRY_ENVIRONMENT = "production"
SENTRY_APP_PACKAGE_NAME = "company_cms"
SENTRY_EXTRA_INTEGRATIONS = [RedisIntegration()]  # Add Redis integration to Sentry SDK
SENTRY_EXTRA_OPTS = {
    "before_send": before_send_filter,  # Do some events filtering before sending them (see: https://docs.sentry.io/platforms/python/configuration/filtering/)
}

# Your Django configuration ...
```

## License

This project is released under [BSD-3 Clause](LICENSE.md).
