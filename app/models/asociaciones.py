from sqlalchemy import Table, Column, Integer, ForeignKey
from app.core.database import Base

# ============================================================
# TABLAS INTERMEDIAS 
# ============================================================
# Se usan objetos Table (no clases) porque estas tablas son
# "invisibles" para la lógica de negocio: no tienen ID propio
# ni atributos, solo unen las claves primarias de otras tablas.
# ============================================================


# Puente entre Usuarios y Roles
# Un usuario puede tener varios roles.
# Un rol puede pertenecer a varios usuarios.

usuario_rol_asoc = Table(
    "usuario_rol",
    Base.metadata,
    Column("usuario_id", Integer, ForeignKey("usuarios.id"), primary_key=True),
    Column("rol_id", Integer, ForeignKey("roles.id"), primary_key=True)
)



# Puente entre Participantes y Relaciones Comerciales
# Un participante puede ser cliente, proveedor, o ambos.
# Una relación comercial puede aplicar a muchos participantes.

participante_relacion_asoc = Table(
    "participante_relacion_comercial",
    Base.metadata,
    Column("participante_id", Integer, ForeignKey("participantes.id"), primary_key=True),
    Column("relacion_comercial_id", Integer, ForeignKey("relaciones_comerciales.id"), primary_key=True)
)




# Puente entre Productos y Proveedores (Participantes)
# Un producto puede tener varios proveedores.
# Un participante puede proveer varios productos.

producto_proveedor_asoc = Table(
    "producto_proveedor",
    Base.metadata,
    Column("producto_id", Integer, ForeignKey("productos.id"), primary_key=True),
    Column("proveedor_id", Integer, ForeignKey("participantes.id"), primary_key=True)
)