from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_session
from app.schemas.rol import RolCreate, RolUpdate, RolResponse
from app.crud import rol as crud

router = APIRouter(prefix="/roles", tags=["Roles"])

@router.get("/", response_model=list[RolResponse])
def listar(db: Session = Depends(get_session)):
    return crud.get_all(db)

@router.get("/{rol_id}", response_model=RolResponse)
def obtener(rol_id: int, db: Session = Depends(get_session)):
    rol = crud.get_by_id(db, rol_id)
    if not rol:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rol no encontrado")
    return rol

@router.post("/", response_model=RolResponse, status_code=status.HTTP_201_CREATED)
def crear(data: RolCreate, db: Session = Depends(get_session)):
    return crud.create(db, data)

@router.put("/{rol_id}", response_model=RolResponse)
def actualizar(rol_id: int, data: RolUpdate, db: Session = Depends(get_session)):
    rol = crud.get_by_id(db, rol_id)
    if not rol:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rol no encontrado")
    return crud.update(db, rol, data)

@router.delete("/{rol_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar(rol_id: int, db: Session = Depends(get_session)):
    rol = crud.get_by_id(db, rol_id)
    if not rol:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rol no encontrado")
    crud.delete(db, rol)