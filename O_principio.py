#Realizar 3 ejerccios del segundo prinicpio
#Eejecricio uno Sistema de pagos :
from abc import ABC, abstractmethod
# ===============================
# Interfaces (cumplen con ISP)
# ===============================
print("Sistema de pagos")
class MedioPago(ABC):
    @abstractmethod
    def pagar( self, monto : float) ->None:
        pass
class MedioAhorro (ABC):
    @abstractmethod
    def guardar (self,monto : float)->None:
        pass

class GestorDeuda:
    """Clase que centraliza la deuda global de un usuario."""
    def __init__(self, deuda_inicial: float)->None:
        self.deuda_global = deuda_inicial

    def reducir_deuda(self, monto: float):
        self.deuda_global -= monto
        print(f"📉 Deuda global ahora: {self.deuda_global}")

class TarjetaCredito(MedioPago,MedioAhorro):
    def __init__(self, gestor: GestorDeuda):
        self.gestor = gestor
        self.ahorros =  0
    
    def pagar(self, monto :float)-> None:
        self.gestor.reducir_deuda(monto)
        

    def guardar (self, monto : float) ->None:
        self.ahorros += monto
        print(f"💰 Guardaste {monto}, ahorros actuales: {self.ahorros}")
        
class Prestamo (MedioPago):
    def __init__(self, deuda_inicial :GestorDeuda):
        self.gestor = deuda_inicial

    def pagar (self,monto : float) -> None:
        self.gestor.reducir_deuda(monto)



gestor = GestorDeuda(5000)
Tarjeta = TarjetaCredito(gestor)
Prestar = Prestamo(gestor)
Tarjeta.pagar(700)
Tarjeta.guardar(700)
Prestar.pagar(60)
