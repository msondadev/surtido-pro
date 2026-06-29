from datetime import datetime
from enum import Enum as PyEnum
from sqlalchemy import String, Float, DateTime, ForeignKey, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base
from app.models.enums import EstadoPedido

class Pedido(Base):
    __tablename__ = "pedidos"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    fecha: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    total: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    
    # Columna de estado usando el Enum
    estado: Mapped[EstadoPedido] = mapped_column(PyEnum(EstadoPedido, native_enum=False), default=EstadoPedido.PENDIENTE)
    # SAEnum integra el Enum de Python con MySQL.
    # MySQL crea una columna ENUM que solo acepta los valores definidos.


    # FK hacia participantes (cliente): para quién es el pedido.
    cliente_id: Mapped[int] = mapped_column(ForeignKey("participantes.id"), nullable=False)
    
    # FK hacia usuarios (creado_por): quién registró el pedido en el sistema.
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"), nullable=False)
    
    # FK hacia empleados (repartidor): opcional, se asigna al organizar la entrega.
    repartidor_id: Mapped[int | None] = mapped_column(ForeignKey("empleados.id"), nullable=True)
    # Mapped[int | None] representa la cardinalidad 0..1 del UML.



        # self.detalles: list[DetallePedido] = [] 

