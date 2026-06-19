from enum import Enum

# ......................
# ENUMS: opciones fijas
# ''''''''''''''''''''''

class EstadoPedido(Enum):
    PENDIENTE = "PENDIENTE"
    CONFIRMADO = "CONFIRMADO"
    CANCELADO = "CANCELADO"
    ENTREGADO = "ENTREGADO"


class TipoMovimientoStock(Enum):
    INGRESO = "INGRESO"
    EGRESO = "EGRESO"
    RESERVA = "RESERVA"
    LIBERACION = "LIBERACION"
    AJUSTE = "AJUSTE"


class EstadoPago(Enum):
    PENDIENTE = "PENDIENTE"
    CONFIRMADO = "CONFIRMADO"
    RECHAZADO = "RECHAZADO"
    ANULADO = "ANULADO"


# Con los enums evitamos el error de tipeo.