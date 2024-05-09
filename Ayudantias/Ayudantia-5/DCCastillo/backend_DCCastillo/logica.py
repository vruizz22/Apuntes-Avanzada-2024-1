from PyQt6.QtCore import QObject, pyqtSignal


class Logica(QObject):

    # Señal que provoca que la ventana del dormitorio se cierre
    senal_dormir = pyqtSignal()

    def __init__(self):
        super().__init__()

    def revisar_hora(self, hora):
        # COMPLETAR
        # hora esta en el formato "HH:MM"
        if hora.split(":")[0] not in range(0,25) or hora.split(":")[1] not in range(0,61):
            print("Hora no válida")
        elif hora.split(":")[0] not in range(6, 21):
            self.senal_dormir.emit()
        
