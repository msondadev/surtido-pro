from datetime import date
from detalle_pedido import DetallePedido
from enums import EstadoPedido
from participante import Participante
from producto import Producto
from usuario import Usuario

class Pedido:
    def __init__(self, id: int, fecha: str, estado: EstadoPedido, total: float, cliente: Participante, usuario: Usuario):
        self.id = id
        self.fecha = fecha
        self.estado = estado
        self.total = total
        self.cliente = cliente # Puede ser PersonaFisica o Empresa
        self.usuario = usuario
        self.detalles: list[DetallePedido] = [] 

    def agregarProducto(self, producto: Producto, cantidad: int):
        # Agrega un producto al pedido creando un DetallePedido asociado. 
        pass
    
    def calcularTotal(self):
        # Suma los subtotales de todos los detalles y actualiza self.total.
        pass

    def confirmarPedido(self):
        # Confirma, descuenta stock reservado y actualiza el estado.
        pass

    def cancelarPedido(self):
        # Cancela y libera el stock previamente reservado.
        pass

    def cambiarEstado(self):
        # Actualiza el estadod el pedido según lo elegido. 
        pass