import graphene

from serializers import (
    TenantGrapheneModel,
)

from models.tenant import Tenant


class Query(graphene.ObjectType):
    say_hello = graphene.String(email=graphene.String(default_value="test"))
    list_all_tenants = graphene.List(TenantGrapheneModel)
    get_single_tenant = graphene.Field(
        TenantGrapheneModel, email=graphene.String()
    )

    @staticmethod
    def resolve_say_hello(parent, info, email):
        return f"hello {email}"

    @staticmethod
    def resolve_list_all_tenants(parent, info):
        return Tenant.all()

    @staticmethod
    def resolve_get_single_tenant(parent, info, email):
        return Tenant.find_or_fail(email)
