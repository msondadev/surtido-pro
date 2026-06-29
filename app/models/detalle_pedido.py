from sqlalchemy import String, Integer, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class DetallePedido(Base):
    __tablename__ = "detalles_pedido"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    
    cantidad: Mapped[int] = mapped_column(Integer, nullable=False)
    precio_unitario: Mapped[float] = mapped_column(Float, nullable=False)
    tipo_precio: Mapped[str] = mapped_column(String(50), nullable=False) 
    # "minorista" o "mayorista": determina qué precio se aplicó al momento
    # de la venta. Se guarda como string para mantener el historial,
    # incluso si el precio del producto cambia en el futuro.

    # FK hacia pedidos: el pedido al que pertenece este detalle.
    # Si se elimina el pedido, sus detalles también desaparecen (composición).
    pedido_id: Mapped[int] = mapped_column(ForeignKey("pedidos.id"), nullable=False)
    
    # FK hacia productos: el producto vendido en este renglón.
    producto_id: Mapped[int] = mapped_column(ForeignKey("productos.id"), nullable=False)