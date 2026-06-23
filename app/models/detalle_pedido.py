from app.models.producto import Producto

class DetallePedido:
    def __init__(self, id: int, cantidad: int, precio_unitario: float, tipo_precio: str, producto: Producto):
        self.id = id
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.tipo_precio = tipo_precio # Minorista o Mayorista
        self.producto = producto

    def calcularSubtotal(self):
        # Retorna el resultado de cantidad * precio_unitario.
        pass