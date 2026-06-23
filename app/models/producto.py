from app.models.categoria import Categoria
from app.models.participante import Participante
class Producto:
    # categoria va por parámetro porque un producto no puede existir sin una categoría. 
    def __init__(self, id: int, nombre: str, precio_minorista: float, precio_mayorista: float, stock_actual: int, stock_reservado: int, 
                foto_url: str, activo: bool, categoria: Categoria):
        
        self.id = id
        self.nombre = nombre
        self.precio_minorista = precio_minorista
        self.precio_mayorista = precio_mayorista
        self.stock_actual = stock_actual
        self.stock_reservado = stock_reservado
        self.foto_url = foto_url
        self.activo = activo
        self.categoria = Categoria
        self.proveedores: list[Participante] = []

    def reservarStock(self):
        # Incrementa el stock reservado al confirmar un pedido pendiente. 
        pass
    
    def liberarStock(self):
        # Decrementa el stock reservado al cancelar un pedido. 
        pass
    
    def actualizarStock(self):
        # Ajusta el stock actual al confirmar entrega o registrar un movimiento.
        pass
