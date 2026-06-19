from participante import Participante

class Empresa(Participante):
    def __init__(self, id: int, email: str, telefono: str, direccion:str, razon_social: str, cuit: str):
        super().__init__(id, email, telefono, direccion)

        self.razon_social = razon_social
        self.cuit = cuit    

    def obtener_nombre_completo():
        # Retorna la razón social de la empresa.
        pass