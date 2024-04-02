from collections import deque, namedtuple
from typing import List


Cancion = namedtuple('Cancion', ['nombre', 'artista'])


class DCCancionero:
    def __init__(self) -> None:
        self.canciones = [] # lista [Cancion(nombre, artista), Cancion(nombre, artista), ...]
        self.cola = deque() # deque
        self.playlists = {} # dict
        self.historial = [] # lista [Cancion(nombre, artista), Cancion(nombre, artista), ...]

    def cargar_canciones(self) -> None:
        with open('canciones.dat') as archivo:
            '''
            Esta linea ingresa una lista de instancias, con compresion de listas
            Itera para cada linea en archivo
            Genera una nametumppled que desempaqueta en 2 elementos con el operador * desempaquetador
            finalmente la lista queda de la forma [Cancion(nombre, artista), Cancion(nombre, artista), ...]
            '''
            self.canciones = [Cancion(*linea.strip().split(',')) for linea in archivo] 

    def agregar_a_la_cola(self, *args) -> None: 
        '''
        Aqui *args significa que es para 1 o más canciones
        En caso de no recibir args, agrega a la cola
        la última canción del hhistorial del usario
        '''
        if len(args) == 0:
            if self.historial: #Esto solo puedo hacerlo si existe historial
                self.cola.append(self.historial[-1])
        elif len(args) == 1:
            self.cola.append(args[0])
            '''
            self.cola.add(args[0]) esta linea no funciona
            No podemos usar add porque es un deque
            Eso es porque add es para sets
            En cambio append es para listas y deque
            '''
    def escuchar_siguiente_cancion(self) -> None:
        '''
        Se escucha la siguiente canción en la cola
        Si esta esta vacía se avisa en consola
        '''
        if len(self.cola) > 0:
            siguiente = self.cola.popleft()
            self.historial.append(siguiente)
            print(f'Escuchando {siguiente.nombre} de {siguiente.arista}')
        else:
            print("Error, la cola esta vacía")
    
    def crear_playlist(self, nombre: str, canciones: List[Cancion]=None) -> None:
        self.playlists[nombre] = set()
        playlist = self.playlists[nombre]
        if canciones is not None:
            for cancion in canciones:
                playlist.add(cancion)
        print(f'Playlist "{nombre}" creada correctamente con {len(playlist)} cancion(es).')

    def escuchar_playlist(self, nombre: str) -> None:
        pass

    def agregar_a_playlist(self, nombre_playlist: str, cancion: Cancion) -> None:
        pass


if __name__ == '__main__':
    cancionero = DCCancionero()
    cancionero.cargar_canciones()
    print(cancionero.canciones)