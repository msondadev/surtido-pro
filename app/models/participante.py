from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base
from app.models.relacion_comercial import RelacionComercial

class Participante(Base):
    """
    Representa cualquier actor del negocio: clientes, proveedores, empleados.
    Nunca se instancia directamente — siempre a través de PersonaFisica o Empresa.

    Estrategia: Joined Table Inheritance.
    Cada subclase tiene su propia tabla con sus atributos específicos,
    vinculada a esta tabla base mediante una Foreign Key.
    """

    __tablename__ = "participantes"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    telefono: Mapped[str | None] = mapped_column(String(20))
    direccion: Mapped[str | None] = mapped_column(String(255))


    # Columna discriminadora:
    tipo_participante: Mapped[str] = mapped_column(String(30))   
    # SQLAlchemy la usa para saber qué subclase es cada fila. Se llama convencionalmente 'tipo'.
    # Valores posibles: 'persona_fisica', 'empresa', 'empleado'.


    __mapper_args__ = {
        "polymorphic_on": "tipo_participante",  # Le dice a SQLAlchemy qué columna usar para distinguir subclases.
        "polymorphic_identity": "participante"  # None porque Participante no se instancia directamente.
    }

# self.relaciones_Comerciales = list[RelacionComercial] = []  


# ====================
# HIJA: Persona Física
# ====================
class PersonaFisica(Participante):
    __tablename__ = "personas_fisicas"

    # Es una FK que apunta al id de la tabla padre (participantes).
    id: Mapped[int] = mapped_column(ForeignKey("participantes.id"), primary_key=True)
    
    # Fijate que ahora podemos sacar el "| None", exigiendo que estos datos existan sí o sí
    nombre: Mapped[str] = mapped_column(String(50), nullable=False)
    apellido: Mapped[str] = mapped_column(String(50), nullable=False)
    dni: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    fecha_nacimiento: Mapped[str | None]

    __mapper_args__ = {
        "polymorphic_identity": "persona_fisica"
    }

    #self.relaciones_Comerciales = list[RelacionComercial] = []  


# ==============
# HIJA: Empresa
# ==============
class Empresa(Participante):
    """
    Tabla para personas jurídicas (empresas clientes o proveedoras).
    Se une a 'participantes' mediante el id (Foreign Key).
    """

    __tablename__ = "empresas"

    id: Mapped[int] = mapped_column(ForeignKey("participantes.id"), primary_key=True)
    
    razon_social: Mapped[str] = mapped_column(String(100), nullable=False)
    cuit: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "empresa"
    }



# =========================================
# NIETA: Empleado (hereda de PersonaFisica)
# =========================================
class Empleado(PersonaFisica):
    __tablename__ = "empleados"

    # Su clave foránea apunta a la tabla de PersonaFisica
    id: Mapped[int] = mapped_column(ForeignKey("personas_fisicas.id"), primary_key=True)
    
    legajo: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)

    fecha_ingreso: Mapped[str | None]

    __mapper_args__ = {
        "polymorphic_identity": "empleado"
    }










