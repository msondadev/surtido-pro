from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_session
from app.schemas.producto import ProductoCreate, ProductoUpdate, ProductoResponse
from app.crud import producto as crud

router = APIRouter(prefix="/productos", tags=["Productos"])

@router.get("/", response_model=list[ProductoResponse])
def listar(db: Session = Depends(get_session)):
    return crud.get_all(db)

@router.get("/{producto_id}", response_model=ProductoResponse)
def obtener(producto_id: int, db: Session = Depends(get_session)):
    producto = crud.get_by_id(db, producto_id)
    if not producto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")
    return producto

@router.post("/", response_model=ProductoResponse, status_code=status.HTTP_201_CREATED)
def crear(data: ProductoCreate, db: Session = Depends(get_session)):
    return crud.create(db, data)

@router.put("/{producto_id}", response_model=ProductoResponse)
def actualizar(producto_id: int, data: ProductoUpdate, db: Session = Depends(get_session)):
    producto = crud.get_by_id(db, producto_id)
    if not producto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")
    return crud.update(db, producto, data)

@router.delete("/{producto_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar(producto_id: int, db: Session = Depends(get_session)):
    producto = crud.get_by_id(db, producto_id)
    if not producto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")
    crud.delete(db, producto)