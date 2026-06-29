from fastapi import FastAPI
from sqlalchemy import text
from app.core.database import engine

app = FastAPI(
    title="Surtido Pro",
    description="Sistema de gestión para distribuidoras y emprendimientos mayoristas-minoristas.",
    version="0.1.0"
)


@app.get("/")
def root():
    """Endpoint raíz. Confirma que la API está corriendo."""
    return {"message": "Surtido Pro API"}


@app.get("/health")
def health_check():
    """Endpoint de salud. Usado para verificar el estado del servidor."""
    return {"status": "ok"}


@app.get("/db-test")
def db_test():
    """
    Prueba la conexión a MySQL ejecutando SELECT 1.
    Si responde 'connected', toda la cadena .env → config → engine → MySQL funciona.
    """
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    return {"database": "¡Conexión a MySQL exitosa!"}