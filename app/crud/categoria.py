from sqlalchemy.orm import Session
from app.models.categoria import Categoria
from app.schemas.categoria import CategoriaCreate, CategoriaUpdate

def get_all(db: Session) -> list[Categoria]:
    return db.query(Categoria).all()

def get_by_id(db: Session, categoria_id: int) -> Categoria | None:
    return db.query(Categoria).filter(Categoria.id == categoria_id).first()

def create(db: Session, data: CategoriaCreate) -> Categoria:
    nueva = Categoria(nombre=data.nombre)
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva

def update(db: Session, categoria: Categoria, data: CategoriaUpdate) -> Categoria:
    categoria.nombre = data.nombre
    db.commit()
    db.refresh(categoria)
    return categoria

def delete(db: Session, categoria: Categoria) -> None:
    db.delete(categoria)
    db.commit()