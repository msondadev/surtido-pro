from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class Rol(Base): # Le dice a SQLAlchemy: Esta clase forma parte del modelo de la BD.
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True) # Nueva forma con SQLAlchemy 2.x 
    
    '''
    Antes:
    id = Column(Integer, primary_key=True, index=True)
    '''
    nombre: Mapped[str] = mapped_column(unique=True)
    descripcion: Mapped[str | None] = mapped_column(String(255))
    # Mapped[str | None]: Puede ser un texto o un Null en la BD (Descripción opcional) 
