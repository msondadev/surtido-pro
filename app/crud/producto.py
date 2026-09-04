from sqlalchemy.orm import Session
from app.models.producto import Producto
from app.schemas.producto import ProductoCreate, ProductoUpdate

def get_all(db: Session) -> list[Producto]:
    return db.query(Producto).all()

def get_by_id(db: Session, producto_id: int) -> Producto | None:
    return db.query(Producto).filter(Producto.id == producto_id).first()

def create(db: Session, data: ProductoCreate) -> Producto:
    nuevo = Producto(**data.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def update(db: Session, producto: Producto, data: ProductoUpdate) -> Producto:
    for campo, valor in data.model_dump().items():
        setattr(producto, campo, valor)
    db.commit()
    db.refresh(producto)
    return producto

def delete(db: Session, producto: Producto) -> None:
    db.delete(producto)
    db.commit()