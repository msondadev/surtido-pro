from abc import ABC, abstractmethod
from datetime import date
from app.models.enums import EstadoPago


class Pago(ABC):
    def __init__(self, id: int, fecha: date, monto: float, estado: EstadoPago):
        self.id = id
        self.fecha = fecha
        self.monto = monto
        self.estado = estado

    @abstractmethod
    def registrar(self):
        # Persiste el pago en el sistema con estado inicial "PENDIENTE".
        pass

    @abstractmethod
    def confirmar(self):
        # Marca el pago como "CONFIRMADO".
        pass

    @abstractmethod
    def cancelar(self):
        # Anula o rechaza el pago.
        pass

