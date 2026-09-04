from sqlalchemy.orm import Session
from app.models.relacion_comercial import RelacionComercial
from app.schemas.relacion_comercial import RelacionComercialCreate, RelacionComercialUpdate

def get_all(db: Session) -> list[RelacionComercial]:
    return db.query(RelacionComercial).all()

def get_by_id(db: Session, relacion_id: int) -> RelacionComercial | None:
    return db.query(RelacionComercial).filter(RelacionComercial.id == relacion_id).first()

def create(db: Session, data: RelacionComercialCreate) -> RelacionComercial:
    nueva = RelacionComercial(nombre=data.nombre)
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def update(db: Session, relacion: RelacionComercial, data: RelacionComercialUpdate) -> RelacionComercial:
    relacion.nombre = data.nombre
    db.commit()
    db.refresh(relacion)
    return relacion

def delete(db: Session, relacion: RelacionComercial) -> None:
    db.delete(relacion)
    db.commit()