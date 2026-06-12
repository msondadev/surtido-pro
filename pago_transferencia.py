from metodo_pago import MetodoPago

class PagoTransferencia(MetodoPago):

    def procesar(self, monto: float):
        print(f"Esperando validación de transferencia por ${monto}.")

        
    
    