from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

# Configuración del hashing de contraseñas.
# bcrypt es el algoritmo estándar de la industria para hashear contraseñas.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Configuración del JWT.
# SECRET_KEY: clave secreta para firmar el token. En producción va en el .env.
# ALGORITHM: algoritmo de firma del token.
# ACCESS_TOKEN_EXPIRE_MINUTES: tiempo de expiración del token.
SECRET_KEY = "cambia_esto_por_una_clave_secreta_segura"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def hashear_contrasenia(contrasenia: str) -> str:
    """Convierte una contraseña en texto plano a un hash seguro."""
    return pwd_context.hash(contrasenia)


def verificar_contrasenia(contrasenia_plana: str, contrasenia_hasheada: str) -> bool:
    """Verifica si una contraseña en texto plano coincide con su hash."""
    return pwd_context.verify(contrasenia_plana, contrasenia_hasheada)


def crear_token(data: dict) -> str:
    """
    Genera un JWT con los datos provistos y un tiempo de expiración.
    El token se firma con SECRET_KEY para que no pueda ser falsificado.
    """
    datos = data.copy()
    expiracion = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    datos.update({"exp": expiracion})
    return jwt.encode(datos, SECRET_KEY, algorithm=ALGORITHM)


def verificar_token(token: str) -> dict | None:
    """
    Verifica y decodifica un JWT.
    Retorna los datos del token si es válido, None si no lo es.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None