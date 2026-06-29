from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base


class Categoria(Base):

    __tablename__ = "categorias"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    
    # Ej: "Bebidas", "Limpieza". No puede estar vacío ni repetirse.
    nombre: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    


# La lista productos: List[Producto]  
# Queda pendiente cuando haga las relacioens. 


