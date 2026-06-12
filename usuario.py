from rol import Rol

class Usuario:
    def __init__(self, id: int, nombre: str, email: str, password: str, roles: list[Rol]):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.password = password
        self.roles = []  # List<Rol>

    def login(self):
        pass

    def cambiar_contrasenia(self, nueva: str):
        pass

    def crear_pedido(self):
        pass

    def ver_pedidos(self):
        pass

    def gestionar_productos(self):
        pass