from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class RelacionComercial(Base):
    """
    Define si un participante actúa como: 
       * CLIENTE 
       * PROVEEDOR 
       * o ambos
    """

    __tablename__ = "relaciones_comerciales"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)


# Pendiente de una tabla intermedia
