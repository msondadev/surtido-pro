from pydantic import BaseModel

# Base con los campos comunes
class CategoriaBase(BaseModel):
    nombre: str

# Para crear (lo que llega en el POST)
class CategoriaCreate(CategoriaBase):
    pass

# Para actualizar (lo que llega en el PUT)
class CategoriaUpdate(CategoriaBase):
    pass

# Para responder (lo que devuelve la API)
class CategoriaResponse(CategoriaBase):
    id: int

    model_config = {"from_attributes": True}