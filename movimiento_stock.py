from datetime import date
from enums import TipoMovimientoStock
from producto import Producto
from usuario import Usuario


class MovimientoStock:
    def __init__(self, id: int, fecha: date, tipo: TipoMovimientoStock, cantidad: int, obervacion: str, producto: Producto, usuario: Usuario):
        self.id = id
        self.fecha = fecha
        self.tipo = tipo
        self.cantidad = cantidad
        self.observacion = obervacion
        self.producto = producto
        self.usuario = usuario

        