from xmlrpc.client import DateTime
from app.models.pedido import Pedido
from app.models.rol import Rol

class Usuario:
    def __init__(
        self, 
        id: int, 
        username: str, 
        contrasenia: str, 
        activo: bool, 
        email_verificado: bool, 
        creado_en: DateTime, 
    ):
        self.id = id
        self.username = username
        self.contrasenia = contrasenia
        self.activo = activo
        self.email_verificado = email_verificado
        self.creado_en = creado_en 
        
        # Las listas arrancan vacías xq el usuario se crea s/roles ni pedidos asignados.
        self.roles = []  # Una forma de escribirlo
        self.pedidos: list[Pedido] = []  # Otra forma de escribirlo


    def login(self):
        pass

    def cerrarSesion(self):
        pass

    def recuperarContrasenia(self):
        pass

    def cambiarContrasenia(self, nueva: str):
        pass    

