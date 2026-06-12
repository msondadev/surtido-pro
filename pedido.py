from datetime import date
from cliente import Cliente
from usuario import Usuario
from detalle_pedido import DetallePedido

class Pedido:
    def __init__(self, id: int, fecha: str, estado: str, cliente: Cliente, usuario: Usuario, total: float, detalles: list[DetallePedido]):
        self.id = id
        self.fecha = fecha
        self.estado = estado
        self.cliente = cliente
        self.usuario = usuario
        self.detalles = []  # List<DetallePedido>
        self.total = total

    def calcular_total(self):
        pass

    def confirmar_pedido(self):
        pass

    def cancelar_pedido(self):
        pass

    def cambiar_estado(self, nuevo_estado: str):
        pass