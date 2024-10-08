from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from .schema import schema
from .sentry import init_sentry

init_sentry()

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
