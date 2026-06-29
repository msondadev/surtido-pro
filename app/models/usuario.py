from datetime import datetime
from sqlalchemy import ForeignKey, String
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.asociaciones import usuario_rol_asoc


class Usuario(Base):
    """
    Representa la tabla 'usuarios' en la base de datos.
    Cuenta de acceso al sistema. Se asocia opcionalmente a un Participante
    cuando ese participante necesita loguearse (ej: Empleado, Cliente registrado).
    """

    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True) # saco autoincrement=True --> SQLAlchemy lo aplica solo. 
    username: Mapped[str] = mapped_column(String(50), unique=True)
    contrasenia: Mapped[str] = mapped_column(String(255))
    activo: Mapped[bool] = mapped_column(default=True)
    email_verificado: Mapped[bool] = mapped_column(default=False)
    
    #  server_default le delega la generación de la fecha a MySQ, no a Python.
    creado_en: Mapped[datetime] = mapped_column(server_default=func.now())

    # FK hacia participantes (0..1)
    # Agregado unique=True para que la relación sea estrictamente 1 a 1
    participante_id: Mapped[int | None] = mapped_column(
        ForeignKey("participantes.id"), nullable=True, unique=True
    )

    # Relationships
    roles: Mapped[list["Rol"]] = relationship(
        "Rol",
        secondary=usuario_rol_asoc,
        back_populates="usuarios"
    )

    # Agregado back_populates="usuario"
    participante: Mapped["Participante | None"] = relationship(
        "Participante",
        foreign_keys=[participante_id],
        back_populates="usuario" 
    )

    pedidos: Mapped[list["Pedido"]] = relationship(
        "Pedido",
        back_populates="usuario",
        foreign_keys="Pedido.usuario_id"
    )

    movimientos_stock: Mapped[list["MovimientoStock"]] = relationship(
        "MovimientoStock",
        back_populates="usuario"
    )

