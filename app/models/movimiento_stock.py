from datetime import date
from app.models.enums import TipoMovimientoStock
from app.models.producto import Producto
from app.models.usuario import Usuario


class MovimientoStock:
    def __init__(self, id: int, fecha: date, tipo: TipoMovimientoStock, cantidad: int, obervacion: str, producto: Producto, usuario: Usuario):
        self.id = id
        self.fecha = fecha
        self.tipo = tipo
        self.cantidad = cantidad
        self.observacion = obervacion
        self.producto = producto
        self.usuario = usuario

        