'''
Este ejercicio busca cubrir los conceptos revisados en 
Estructuras de datos buitls-ins.
'''

'''
La idea del ejercicio es simular una version simplificada de un juego.
Para esto utilizaremos el archivo cards.csv
'''

from collections import namedtuple
from random import shuffle, choice, randint  # Puedes utilizar estas funciones si lo deseas

class Juego:

    def __init__(self, turnos):

        self.mazo = []
        self.cartas_j1 = []
        self.cartas_j2 = []

        self.read_file()
        self.repartir_cartas()
        self.comenzar_juego(turnos)

    def read_file(self):
        '''
        Leer las cartas y guardarlas en una estructura de datos adecuada
        Creamos un diccionario que tendra cada carta
        Luego guardamos las llaves de cada carta en la lista mazo
        '''
        cartas = {}
        with open("cards.csv", "r", encoding="utf-8") as archivo:
            primera_linea = archivo.readline().strip().split(",")
            # Creamos una clase llamada Carta
            Carta = namedtuple('Carta', primera_linea)
            for linea in archivo:
                # Guardamos en variables su nombre, ataque y defensa
                nombre, ataque, defensa = linea.strip().split(",")
                '''
                Finalmente creamos una clase de la carta
                y la guardamos asociada a una llave con su nombre
                en el dict mazo_cartas
                '''
                carta = Carta(nombre, ataque, defensa)
                cartas[nombre] = carta
        self.mazo = list(cartas.keys())

    def repartir_cartas(self):
        '''
        Barajar las cartas y repartirlas de a 1
        Cada jugador recibirá 5 cartas
        Para ello mezclamos el mazo 
        Y elegimos aletoriamente una carta para cada uno
        '''
        mazo_barajado = shuffle(self.mazo)
        for contador in range(5):
            self.cartas_j1.append(mazo_barajado.choice())
            self.cartas_j2.append(mazo_barajado.choice())
        
        pass

    def atacar(self, atacante, defensa):
        ptos_ataque = atacante.ataque
        ptos_defensa = defensa.defensa
        # Rellenar aquí

    def comenzar_juego(self, turnos):
        for i in range(1, turnos + 1):
            print(f"Turno número {i}")
            if i % 2:
                # Ataca el jugador 1
                # Rellenar aquí
                pass
            else:
                # Ataca el jugador 2
                # Rellenar aquí
                pass
            
            # Si alguno de los jugadores se queda sin cartas, termina la partida
            if not (len(self.cartas_j1) and len(self.cartas_j2)):
                print('Ha terminado la partida')
                break


juego = Juego(10)