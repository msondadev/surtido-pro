from sqlalchemy import String, Boolean, Float, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

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





        # self.categoria = Categoria
        # self.proveedores: list[Participante] = []

