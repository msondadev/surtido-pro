from fastapi import FastAPI
from sqlalchemy import text
from app.core.database import engine

# Importar todos los modelos para que SQLAlchemy registre los relationships
from app.models import (
    asociaciones,
    categoria, producto, participante,
    relacion_comercial, usuario, rol,
    pedido, detalle_pedido, pago, movimiento_stock
)

from app.routers import categorias as categorias_router
from app.routers import roles as roles_router
from app.routers import productos as productos_router
from app.routers import relaciones_comerciales as relaciones_router
from app.routers.auth import router as auth_router

app = FastAPI(
    title="Surtido Pro",
    description="Sistema de gestión para distribuidoras y emprendimientos mayoristas-minoristas.",
    version="0.1.0"
)

app.include_router(categorias_router.router)
app.include_router(roles_router.router)
app.include_router(productos_router.router) 
app.include_router(relaciones_router.router)
app.include_router(auth_router)


@app.get("/")
def root():
    return {"message": "Surtido Pro API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/db-test")
def db_test():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    return {"database": "¡Conexión a MySQL exitosa!"}
