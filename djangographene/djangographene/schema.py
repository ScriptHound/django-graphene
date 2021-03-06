import graphene
from main.schema import Query as main_query


class Query(main_query):
    pass


schema = graphene.Schema(query=Query)
