from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_session
from app.schemas.relacion_comercial import RelacionComercialCreate, RelacionComercialUpdate, RelacionComercialResponse
from app.crud import relacion_comercial as crud

router = APIRouter(prefix="/relaciones-comerciales", tags=["Relaciones Comerciales"])

@router.get("/", response_model=list[RelacionComercialResponse])
def listar(db: Session = Depends(get_session)):
    return crud.get_all(db)

@router.get("/{relacion_id}", response_model=RelacionComercialResponse)
def obtener(relacion_id: int, db: Session = Depends(get_session)):
    relacion = crud.get_by_id(db, relacion_id)
    if not relacion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Relación comercial no encontrada")
    return relacion

@router.post("/", response_model=RelacionComercialResponse, status_code=status.HTTP_201_CREATED)
def crear(data: RelacionComercialCreate, db: Session = Depends(get_session)):
    return crud.create(db, data)

@router.put("/{relacion_id}", response_model=RelacionComercialResponse)
def actualizar(relacion_id: int, data: RelacionComercialUpdate, db: Session = Depends(get_session)):
    relacion = crud.get_by_id(db, relacion_id)
    if not relacion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Relación comercial no encontrada")
    return crud.update(db, relacion, data)

@router.delete("/{relacion_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar(relacion_id: int, db: Session = Depends(get_session)):
    relacion = crud.get_by_id(db, relacion_id)
    if not relacion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Relación comercial no encontrada")
    crud.delete(db, relacion)