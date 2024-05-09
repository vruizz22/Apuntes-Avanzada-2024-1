import os
from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QWidget, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import pyqtSignal


class Castillo(QWidget):

    senal_abrir_ventana = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle("¡ Castillo !")
        self.setGeometry(0, 0, 500, 500)

        # Crear el contenedor para los botones
        imagen_ruta = os.path.join("imagenes_DCCastillo", "lobby_DCCastillo.jpg")
        label_imagen = QLabel(self)
        pixeles = QPixmap(imagen_ruta)
        label_imagen.setPixmap(pixeles)
        label_imagen.setScaledContents(True)
        label_imagen.setFixedSize(500, 500)

        # Creamos los botones (COMPLETAR)
        boton_dormitorio = QPushButton("Dormitorio", self)
        boton_bano = QPushButton("Baño", self)
        boton_salir = QPushButton("Salir", self)
        

        # Conectamos las señales (COMPLETAR)
        boton_dormitorio.clicked.connect(self.metodo_abrir_dormitorio)
        boton_bano.clicked.connect(self.metodo_abrir_bano)
        boton_salir.clicked.connect(self.close)

        # Creamos el layout y añadimos los widgets
        layout_vertical = QVBoxLayout()
        layout_vertical.addStretch(1)
        layout_vertical.addWidget(label_imagen)
        layout_vertical.addWidget(boton_dormitorio)
        layout_vertical.addWidget(boton_bano)
        layout_vertical.addWidget(boton_salir)
        layout_vertical.addStretch(1)

        # COMPLETAR
        self.setLayout(layout_vertical)

    # En el caso que se clickee el boton Dormitorio
    def metodo_abrir_dormitorio(self):
        self.hide()
        self.senal_abrir_ventana.emit("Dormitorio")

    # En el caso que se clickee el boton Baño
    def metodo_abrir_bano(self):
        self.hide()
        self.senal_abrir_ventana.emit("Baño")

    # Para cuando se necesite abrir nuevamente
    def abrir_nuevamente(self):
        self.show()
        
