from producto import Producto

class DetallePedido:
    def __init__(self, producto: Producto, cantidad: int, precio_unitario: float, subtotal: float):
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.subtotal = subtotal

    def calcular_subtotal(self):
        pass