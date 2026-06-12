class Producto:
    def __init__(self, id: int, nombre: str, precio_minorista: float, precio_mayorista: float, stock_actual: int, stock_reservado: int):
        self.id = id
        self.nombre = nombre
        self.precio_minorista = precio_minorista
        self.precio_mayorista = precio_mayorista
        self.stock_actual = stock_actual
        self.stock_reservado = stock_reservado

    def actualizar_stock(self, cantidad: int):
        pass

    def reservar_stock(self, cantidad: int):
        pass

    def liberar_stock(self, cantidad: int):
        pass