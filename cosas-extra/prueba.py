'''
import collections

class Banco:
    def __init__(self, dinero):
        self.dinero_setter(dinero)
        self.historial = collections.deque()
        
    @property
    def dinero(self):
        self.historial.appendleft(self._dinero_guardado)
        self.dinero = 2
        return self.historial[-1]
    
    @dinero.setter
    def dinero(self, dinero):
        print("Entre :)")
        self._dinero_guardado += dinero
        self.historial.append(self._dinero_guardado)
        
    def dinero_setter(self, dinero):
        self._dinero_guardado = dinero
        
    
banco = Banco(1)
banco.dinero = banco.dinero + 2
dinero = banco.dinero
print(banco.historial)

'''

cantidad = 10
print("*** Menú de inicio ***")
print()
print("Dinero disponible:", "5")
print()
print(" " * 7 + "Producto" + " " * 6 + "Precio")
print(f"[1] Gato Mago {cantidad:^20d}")
print(f"[2] Gato Guerrero {cantidad:^13d}")
print(f"[3] Gato Cabañero {cantidad:^13d}")
print(f"[4] Ítem Armadura {cantidad:^13d}")
print(f"[5] Ítem Pergamino {cantidad:^10d}")
print(f"[6] Ítem Lanza {cantidad:^19d}")
print(f"[7] Ítem Cura {cantidad:^20d}")
print()
print("[0] Volver al Menú de inicio")