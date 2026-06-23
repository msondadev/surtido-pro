from datetime import date
from app.models.enums import EstadoPago
from app.models.pago import Pago

class PagoEfectivo(Pago):
    def __init__(self, id: int, fecha: date, monto: float, estado: EstadoPago, monto_recibido: float, vuelto: float):
        super().__init__(id, fecha, monto, estado)

        self.monto_recibido = monto_recibido
        self.vuelto = vuelto

    def procesar(self, monto: float):
        print(f"Procesando ${monto} en efectivo.")


    def validar(self):
        pass    

    def registrar(self):
        pass    

    def confirmar(self):
        pass 

    def cancelar(self):
        pass       