from pydantic import BaseModel

class ProductoBase(BaseModel):
    nombre: str
    descripcion: str | None = None
    foto_url: str | None = None
    precio_minorista: float
    precio_mayorista: float
    stock_actual: int = 0
    stock_reservado: int = 0
    activo: bool = True
    categoria_id: int

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(ProductoBase):
    pass

class ProductoResponse(ProductoBase):
    id: int

    model_config = {"from_attributes": True}