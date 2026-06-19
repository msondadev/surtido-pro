from datetime import date
from enums import EstadoPago
from pago import Pago

class PagoTransferencia(Pago):
    def __init__(self, id: int, fecha: date, monto: float, estado: EstadoPago, cbu: str, alias: str, comprobante_url: str):
        super().__init__(id, fecha, monto, estado)

        self.cbu = cbu
        self.alias = alias
        self.comprobante_url = comprobante_url


    def procesar(self, monto: float):
        # Registra los datos de la transf para su posterior validación.
        print(f"Esperando validación de transferencia por ${monto}.")

    def validar(self):
        # Verifica el comprobante de transferencia antes de confirmar.
        pass    

    def registrar(self):
        pass    

    def confirmar(self):
        # Confirma la transferencia una vez validado el comprobante.
        pass 

    def cancelar(self):
        # Rechaza o anula la transferencia.
        pass  