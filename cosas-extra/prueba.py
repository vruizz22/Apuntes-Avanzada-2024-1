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