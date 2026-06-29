from datetime import datetime
from enum import Enum as PyEnum
from sqlalchemy import String, Float, DateTime, ForeignKey, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base
from app.models.enums import EstadoPago

class Pago(Base):
    """
    Estrategia: Joined Table Inheritance.
    Cada subclase tiene su propia tabla con sus atributos específicos,
    vinculada a esta tabla base mediante una Foreign Key.
    """

    __tablename__ = "pagos"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    fecha: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    monto: Mapped[float] = mapped_column(Float, nullable=False)

    #Enum
    estado: Mapped[EstadoPago] = mapped_column(PyEnum(EstadoPago, native_enum=False), default=EstadoPago.PENDIENTE)
    
    # FK hacia pedidos: el pedido al que corresponde este pago.
    pedido_id: Mapped[int] = mapped_column(ForeignKey("pedidos.id"), nullable=False)
    

    # Columna discriminadora: identifica qué subclase es cada fila.
    # Valores posibles: 'efectivo', 'transferencia', 'mercado_pago'.
    tipo_pago: Mapped[str] = mapped_column(String(30))

    __mapper_args__ = {
        "polymorphic_on": "tipo_pago",
        "polymorphic_identity": None
    }


# ====================
# Hijas
# ====================
class PagoEfectivo(Pago):
    __tablename__ = "pagos_efectivo"

    id: Mapped[int] = mapped_column(ForeignKey("pagos.id"), primary_key=True)
    monto_recibido: Mapped[float] = mapped_column(Float, nullable=False)
    vuelto: Mapped[float] = mapped_column(Float, nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "efectivo"
    }


class PagoTransferencia(Pago):
    __tablename__ = "pagos_transferencia"

    id: Mapped[int] = mapped_column(ForeignKey("pagos.id"), primary_key=True)
    cbu: Mapped[str] = mapped_column(String(22), nullable=False)
    alias: Mapped[str | None] = mapped_column(String(50))
    comprobante_url: Mapped[str | None] = mapped_column(String(255))

    __mapper_args__ = {
        "polymorphic_identity": "transferencia"
    }


class PagoMercadoPago(Pago):
    __tablename__ = "pagos_mercado_pago"
    id: Mapped[int] = mapped_column(ForeignKey("pagos.id"), primary_key=True)
    
    preference_id: Mapped[str] = mapped_column(String(100), nullable=False)
    payment_id: Mapped[str | None] = mapped_column(String(100))
    external_reference: Mapped[str | None] = mapped_column(String(100))

    __mapper_args__ = {
        "polymorphic_identity": "mercadopago"
    }

