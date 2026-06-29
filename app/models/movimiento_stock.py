from datetime import datetime
from enum import Enum as PyEnum
from sqlalchemy import String, Integer, DateTime, ForeignKey, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base
from app.models.enums import TipoMovimientoStock

class MovimientoStock(Base):
    """
    Registro histórico de cada cambio en el stock de un producto.
    Permite auditoría y trazabilidad completa del inventario.
    """

    __tablename__ = "movimientos_stock"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    fecha: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    cantidad: Mapped[int] = mapped_column(Integer, nullable=False)
    observacion: Mapped[str | None] = mapped_column(String(255))
    
    # Enum
    tipo: Mapped[TipoMovimientoStock] = mapped_column(PyEnum(TipoMovimientoStock, native_enum=False), )


    # FK hacia productos: qué producto fue afectado por el movimiento.
    producto_id: Mapped[int] = mapped_column(ForeignKey("productos.id"), nullable=False)
    
    # FK hacia usuarios: quién generó el movimiento (trazabilidad)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"), nullable=False)





        # self.producto = producto
        # self.usuario = usuario