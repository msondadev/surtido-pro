from sqlalchemy import String, Boolean, Float, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base
from app.models.asociaciones import producto_proveedor_asoc

class Producto(Base):
    __tablename__ = "productos"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    
    # Descripción y foto opcionales
    descripcion: Mapped[str | None] = mapped_column(String(255))
    foto_url: Mapped[str | None] = mapped_column(String(255))
    
    precio_minorista: Mapped[float] = mapped_column(Float, nullable=False)
    precio_mayorista: Mapped[float] = mapped_column(Float, nullable=False)
    
    # Stock (Enteros con valor por defecto en 0 para evitar valores nulos al crear)
    stock_actual: Mapped[int] = mapped_column(Integer, default=0)
    stock_reservado: Mapped[int] = mapped_column(Integer, default=0)
    
    # Estado del producto
    activo: Mapped[bool] = mapped_column(Boolean, default=True)

    # FK hacia categorias (1 categoria por producto)
    categoria_id: Mapped[int] = mapped_column(ForeignKey("categorias.id"), nullable=False)


# relationship
    # Relación N a 1 con Categoria.
    # Muchos productos pertenecen a una categoría.
    
    categoria: Mapped["Categoria"] = relationship(
        "Categoria",
        back_populates="productos"
    )
    # back_populates conecta con productos definido en categoria.py.
 


    # Relación N a N con Participante (proveedores).
    
    proveedores: Mapped[list["Participante"]] = relationship(
        "Participante",
        secondary=producto_proveedor_asoc,
        back_populates="productos_provistos"
    )
    # back_populates conecta con productos_provistos definido en participante.py.



    # Relación 1 a N con MovimientoStock.
    # Un producto puede tener muchos movimientos de stock registrados.
    movimientos_stock: Mapped[list["MovimientoStock"]] = relationship(
        "MovimientoStock",
        back_populates="producto"
    )