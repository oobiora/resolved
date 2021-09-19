import accounts.schema
import services.schema
import graphene

from graphene_django.debug import DjangoDebug



class Query(
    accounts.schema.Query,
    services.schema.Query
):
    debug = graphene.Field(DjangoDebug, name="_debug")

class Mutation(
    accounts.schema.Mutation,
    services.schema.Mutation
):
    debug = graphene.Field(DjangoDebug, name="_debug")

schema = graphene.Schema(query=Query, mutation=Mutation)