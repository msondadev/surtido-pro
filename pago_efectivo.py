from metodo_pago import MetodoPago

class PagoEfectivo(MetodoPago):

    def procesar(self, monto: float):
        print(f"Procesando ${monto} en efectivo.")