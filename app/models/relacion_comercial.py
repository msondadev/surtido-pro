from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from app.models.asociaciones import participante_relacion_asoc

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


# relationship
   
   participantes: Mapped[list["Participante"]] = relationship(
      "Participante",
      secondary=participante_relacion_asoc,
      back_populates="relaciones_comerciales"
   )
   # back_populates conecta con relaciones_comerciales definido en participante.py.