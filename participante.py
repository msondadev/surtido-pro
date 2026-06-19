from abc import ABC, abstractmethod
from relacion_comercial import RelacionComercial

class Participante(ABC):
    def __init__(self, id: int, email: str, telefono: str, direccion: str):
        self.id = id
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.relaciones_Comerciales = list[RelacionComercial] = []  

    @abstractmethod
    def obtener_nombre_completo():
        # Retorna el nombre completo o razón social del participante.
        pass


# Participantes:
#     * Clientes
#     * Proveedores
#     * Empleados