from datetime import date
from app.models.enums import EstadoPago
from app.models.pago import Pago

# Integración con la API de MP.
class PagoMercadoPago(Pago):
    def __init__(self, id: int, fecha: date, monto: float, estado: EstadoPago, preference_id: str, payment_id: str, external_reference: str):
        super().__init__(id, fecha, monto, estado)

        self.preference_id = preference_id
        self.payment_id = payment_id
        self.external_reference = external_reference


    def procesar(self, monto: float):
        # Genera la preferencia de pago y redirige al usuario a Mercado Pago.
        print(f"Esperando validación de pago por ${monto}.")

    def validar(self):
        # Consulta el estado del pago en la API de Mercado Pago.
        pass    

    def registrar(self):
        pass    

    def confirmar(self):
        # Confirma el pago una vez verificado el webhook de Mercado Pago.
        pass 

    def cancelar(self):
        # Cancela o reembolsa el pago en Mercado Pago.
        pass  