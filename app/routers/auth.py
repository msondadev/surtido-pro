from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_session as get_db
from app.core.security import hashear_contrasenia, verificar_contrasenia, crear_token
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate, UsuarioResponse, LoginRequest, TokenResponse

router = APIRouter(prefix="/auth", tags=["Autenticación"])


@router.post("/registro", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def registrar_usuario(datos: UsuarioCreate, db: Session = Depends(get_db)):
    """
    Crea un usuario nuevo con la contraseña hasheada.
    Verifica que el username no esté en uso antes de crear.
    """
    # Verificar si el username ya existe.
    usuario_existente = db.query(Usuario).filter(Usuario.username == datos.username).first()
    if usuario_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El username ya está en uso."
        )

    # Hashear la contraseña antes de guardarla.
    contrasenia_hasheada = hashear_contrasenia(datos.contrasenia)

    # Crear el usuario con la contraseña hasheada.
    nuevo_usuario = Usuario(
        username=datos.username,
        contrasenia=contrasenia_hasheada
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario


@router.post("/login", response_model=TokenResponse)
def login(datos: LoginRequest, db: Session = Depends(get_db)):
    """
    Verifica las credenciales del usuario y devuelve un JWT si son correctas.
    """
    # Buscar el usuario por username.
    usuario = db.query(Usuario).filter(Usuario.username == datos.username).first()

    # Verificar que el usuario existe y la contraseña es correcta.
    if not usuario or not verificar_contrasenia(datos.contrasenia, usuario.contrasenia):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Verificar que el usuario está activo.
    if not usuario.activo:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Usuario inactivo."
        )

    # Generar el JWT con el username como dato principal.
    token = crear_token({"sub": usuario.username, "id": usuario.id})
    return {"access_token": token, "token_type": "bearer"}