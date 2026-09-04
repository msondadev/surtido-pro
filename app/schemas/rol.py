from pydantic import BaseModel

class RolBase(BaseModel):
    nombre: str
    descripcion: str | None = None

class RolCreate(RolBase):
    pass

class RolUpdate(RolBase):
    pass

class RolResponse(RolBase):
    id: int

    model_config = {"from_attributes": True}