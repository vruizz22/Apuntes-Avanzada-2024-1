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
        
        self.cartas = {}
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
                self.cartas[nombre] = carta
                
        self.mazo = list(self.cartas.values())

    def repartir_cartas(self):
        '''
        Barajar las cartas y repartirlas de a 1
        Cada jugador recibirá 5 cartas
        Para ello mezclamos el mazo 
        Y elegimos aletoriamente una carta para cada uno
        '''
        shuffle(self.mazo)
        for contador in range(5):
            self.cartas_j1.append(choice(self.mazo))
            self.cartas_j2.append(choice(self.mazo))
        

    def atacar(self, atacante, defensa):
        '''
        Instancias de Carta
        Retorna True si gana atacante
        False si no
        '''
        ptos_ataque = atacante.ataque
        ptos_defensa = defensa.defensa
        
        if ptos_ataque < ptos_defensa:
            return False
        
        elif ptos_defensa == ptos_ataque:
            # Tirar un dado para elegir quien gana en caso de empate
            while ptos_ataque == ptos_defensa:
                ptos_ataque = randint(1,6)
                ptos_defensa = randint(1,6)
                
            if ptos_ataque < ptos_defensa:
                return False
    
            return True
        
        return True

    def comenzar_juego(self, turnos):
        for i in range(1, turnos + 1):
            print(f"Turno número {i}")

            # Determinar el atacante y el defensor en función del turno
            if i % 2:
                atacante, defensor = self.cartas_j1, self.cartas_j2
            else:
                atacante, defensor = self.cartas_j2, self.cartas_j1

            # Elegir cartas para el ataque y la defensa
            carta_atacante = choice(atacante)
            carta_defensor = choice(defensor)

            # Realizar el ataque
            if self.atacar(carta_atacante, carta_defensor):
                defensor.pop(defensor.index(carta_defensor))
            else:
                atacante.pop(atacante.index(carta_atacante))

            # Comprobar si alguno de los jugadores se ha quedado sin cartas
            if not (len(self.cartas_j1) and len(self.cartas_j2)):
                print('Ha terminado la partida')
                break

        # Determinar quién ganó
        if len(self.cartas_j1) > len(self.cartas_j2):
            print("Ganador: Jugador 1")
        elif len(self.cartas_j1) < len(self.cartas_j2):
            print("Ganador: Jugador 2")
        else:
            print("Empate")
        
juego = Juego(10)