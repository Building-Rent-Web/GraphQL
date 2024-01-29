from models import tenant, building, billing
from typing import List, Optional

from graphene_pydantic import PydanticInputObjectType, PydanticObjectType
from pydantic import BaseModel


class BuildingModel(BaseModel):
    id: int


class BillingModel(BaseModel):
    id: int

class TenantModel(BaseModel):
    id: int
    email: str
    phone_number: str
    name: str    


class BuildingGrapheneModel(PydanticObjectType):
    class Meta:
        model = BuildingModel


class BillingGrapheneModel(PydanticObjectType):
    class Meta:
        model = BillingModel


class TenantGrapheneModel(PydanticObjectType):
    class Meta:
        model = TenantModel


class BuildingGrapheneInputModel(PydanticInputObjectType):
    class Meta:
        model = BuildingModel


class BillingGrapheneInputModel(PydanticInputObjectType):
    class Meta:
        model = BillingModel


class TenantGrapheneInputModel(PydanticInputObjectType):
    class Meta:
        model = TenantModel
