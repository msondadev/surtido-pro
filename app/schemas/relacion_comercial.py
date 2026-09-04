from pydantic import BaseModel

class RelacionComercialBase(BaseModel):
    nombre: str

class RelacionComercialCreate(RelacionComercialBase):
    pass

class RelacionComercialUpdate(RelacionComercialBase):
    pass

class RelacionComercialResponse(RelacionComercialBase):
    id: int

    model_config = {"from_attributes": True}