from pydantic import BaseModel


class UsuarioCreate(BaseModel):
    """Schema para crear un usuario nuevo. Recibe los datos del request."""
    username: str
    contrasenia: str


class UsuarioResponse(BaseModel):
    """Schema de respuesta. Nunca expone la contraseña."""
    id: int
    username: str
    activo: bool
    email_verificado: bool

    class Config:
        from_attributes = True


class LoginRequest(BaseModel):
    """Schema para el request de login."""
    username: str
    contrasenia: str


class TokenResponse(BaseModel):
    """Schema de respuesta del login. Devuelve el JWT."""
    access_token: str
    token_type: str = "bearer"