import sentry_sdk
from sentry_sdk.integrations.strawberry import StrawberryIntegration
import os


def init_sentry():
    sentry_sdk.init(
        debug=True,
        dsn=os.getenv("SENTRY_DSN"),
        enable_tracing=True,
        traces_sample_rate=1.0,
        profiles_sample_rate=1.0,
        integrations=[StrawberryIntegration()],
        auto_enabling_integrations=True,
    )
