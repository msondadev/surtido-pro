from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from app.models.asociaciones import usuario_rol_asoc  # <-- Importamos la tabla puente

class Rol(Base): # Le dice a SQLAlchemy: Esta clase forma parte del modelo de la BD.
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True) # Nueva forma con SQLAlchemy 2.x 
    # Antes:
    # id = Column(Integer, primary_key=True, index=True)

    nombre: Mapped[str] = mapped_column(unique=True)
    descripcion: Mapped[str | None] = mapped_column(String(255))
    # Mapped[str | None]: Puede ser un texto o un Null en la BD (Descripción opcional) 


# relationship

    usuarios: Mapped[list["Usuario"]] = relationship(
        secondary=usuario_rol_asoc,
        back_populates="roles"
    )
    # secondary=usuario_rol_asoc le dice a SQLAlchemy que use la tabla intermedia para buscar
    # 'back_populates' conecta esta relación con la de Usuario,
    # para que ambos lados se mantengan sincronizados automáticamente.