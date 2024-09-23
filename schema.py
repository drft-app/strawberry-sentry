import strawberry
import sentry_sdk
from sentry_sdk.integrations.strawberry import StrawberryIntegration

SENTRY_DSN = ""


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello, world!"


sentry_sdk.init(
    # debug=True,
    dsn=SENTRY_DSN,
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
    integrations=[StrawberryIntegration(async_execution=True)],
    auto_enabling_integrations=True,
)


schema = strawberry.Schema(query=Query)
