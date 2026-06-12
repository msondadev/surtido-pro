from abc import ABC, abstractmethod

class MetodoPago(ABC):
    @abstractmethod
    def procesar(self, monto: float):
        pass

class PagoEfectivo(MetodoPago):
    def procesar(self, monto: float):
        pass

class PagoTransferencia(MetodoPago):
    def procesar(self, monto: float):
        pass