# pyrefly: ignore [missing-import]
from fastapi import APIRouter, Depends, HTTPException, status
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Session
from app.core.database import get_session
from app.schemas.categoria import CategoriaCreate, CategoriaUpdate, CategoriaResponse
from app.crud import categoria as crud

router = APIRouter(prefix="/categorias", tags=["Categorías"])

@router.get("/", response_model=list[CategoriaResponse])
def listar(db: Session = Depends(get_session)):
    return crud.get_all(db)

@router.get("/{categoria_id}", response_model=CategoriaResponse)
def obtener(categoria_id: int, db: Session = Depends(get_session)):
    categoria = crud.get_by_id(db, categoria_id)
    if not categoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categoría no encontrada")
    return categoria

@router.post("/", response_model=CategoriaResponse, status_code=status.HTTP_201_CREATED)
def crear(data: CategoriaCreate, db: Session = Depends(get_session)):
    return crud.create(db, data)

@router.put("/{categoria_id}", response_model=CategoriaResponse)
def actualizar(categoria_id: int, data: CategoriaUpdate, db: Session = Depends(get_session)):
    categoria = crud.get_by_id(db, categoria_id)
    if not categoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categoría no encontrada")
    return crud.update(db, categoria, data)

@router.delete("/{categoria_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar(categoria_id: int, db: Session = Depends(get_session)):
    categoria = crud.get_by_id(db, categoria_id)
    if not categoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categoría no encontrada")
    crud.delete(db, categoria)