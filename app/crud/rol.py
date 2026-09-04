from sqlalchemy.orm import Session
from app.models.rol import Rol
from app.schemas.rol import RolCreate, RolUpdate

def get_all(db: Session) -> list[Rol]:
    return db.query(Rol).all()

def get_by_id(db: Session, rol_id: int) -> Rol | None:
    return db.query(Rol).filter(Rol.id == rol_id).first()

def create(db: Session, data: RolCreate) -> Rol:
    nuevo = Rol(nombre=data.nombre, descripcion=data.descripcion)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def update(db: Session, rol: Rol, data: RolUpdate) -> Rol:
    rol.nombre = data.nombre
    rol.descripcion = data.descripcion
    db.commit()
    db.refresh(rol)
    return rol

def delete(db: Session, rol: Rol) -> None:
    db.delete(rol)
    db.commit()