from datetime import date
from participante import Participante
from relacion_comercial import RelacionComercial

class PersonaFisica(Participante):
    def __init__(self, id: int, email: str, telefono: str, direccion: str, nombre: str, apellido: str, dni: str, fecha_nac: date):
        super().__init__(id, email, telefono, direccion) # Inicializa la clase madre (Participante)
        
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.fecha_nac = fecha_nac
        self.relaciones_Comerciales = list[RelacionComercial] = []  


    def obtener_nombre_completo():
        # Retorna nombre y apellido concatenados.
        pass