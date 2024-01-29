from db import Model


class Tenant(Model):
    id: int
    name: str
    email: str
    phone_number: str
