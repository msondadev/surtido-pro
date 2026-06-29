from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

class Categoria(Base):

    __tablename__ = "categorias"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    
    # Ej: "Bebidas", "Limpieza". No puede estar vacío ni repetirse.
    nombre: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    

# relationship
    # Relación 1 a N con Producto.
    # Una categoría puede tener muchos productos.
    
    productos: Mapped[list["Producto"]] = relationship(
        "Producto",
        back_populates="categoria"
    )
    # back_populates conecta con categoria definido en producto.py.