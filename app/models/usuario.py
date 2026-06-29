from datetime import datetime
from sqlalchemy import String, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class Usuario(Base):
    """
    Cuenta de acceso al sistema. Se asocia opcionalmente a un Participante
    cuando ese participante necesita loguearse (ej: Empleado, Cliente registrado).
    """

    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    
    # La contraseña siempre lleva String(255) porque luego la vamos a guardar encriptada (hasheada)
    contrasenia: Mapped[str] = mapped_column(String(255), nullable=False)
    
    # Booleans con valores por defecto
    activo: Mapped[bool] = mapped_column(Boolean, default=True)
    email_verificado: Mapped[bool] = mapped_column(Boolean, default=False)
    
    # DateTime con func.now() para que MySQL ponga la fecha y hora automática al momento de crearlo
    creado_en: Mapped[datetime] = mapped_column(DateTime, default=func.now())

    # FK hacia participantes (0..1): un Usuario puede estar asociado
    # a un Participante o no. 
    participante_id: Mapped[int] = mapped_column(ForeignKey("participantes.id"), unique=True, nullable=False)
    # unique=True: Garantiza que un Participante no pueda tener dos usuarios distintos.





        # Las listas arrancan vacías xq el usuario se crea s/roles ni pedidos asignados.
        # self.roles = []  # Una forma de escribirlo
        # self.pedidos: list[Pedido] = []  # Otra forma de escribirlo

