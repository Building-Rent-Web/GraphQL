from fastapi import FastAPI
import graphene
import uvicorn
from starlette.graphql import GraphQLApp
from schema import Query

app = FastAPI()
app.add_route(
    "/graphiql", GraphQLApp(schema=graphene.Schema(query=Query))
)


@app.get("/")
def main():
    return {"Hello": "World"}