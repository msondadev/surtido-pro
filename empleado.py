from datetime import date
from persona_fisica import PersonaFisica

class Empleado(PersonaFisica):
    # Es una persona física pero trabaja en la empresa. 
    def __init__(self, id: int, email:str, telefono: str, direccion: str, nombre:str, apellido: str, dni:str, fecha_nac: date, legajo: str, fecha_ingreso: date):
        super().__init__(id, email, telefono, direccion, nombre, apellido, dni, fecha_nac)

        self.legajo = legajo
        self.fecha_ingreso = fecha_ingreso