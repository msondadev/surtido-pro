from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.core.config import settings

# engine: representa la conexión con MySQL
engine = create_engine(settings.DATABASE_URL, echo=True)

# Creamos la fábrica de sesiones
# Cada request de la API abre una sesión, la usa y la cierra
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# La clase base para todos nuestros futuros modelos de SQLAlchemy
# Estándar moderno SQLAlchemy 2.0
class Base(DeclarativeBase):
    pass

# Dependencia para inyectar en las rutas de FastAPI
def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()