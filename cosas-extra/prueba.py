
with open("texto.txt", "r") as archivo:
    data = archivo.readlines()
    info = [line.rstrip('\n') for line in data]
    print(info)
    numeros = info[-1].split(",")
    print(numeros)
    lista_red = []
    cantidad_de_estaciones = int(info[0])
    for contador in range(cantidad_de_estaciones):
        lista_red.append(numeros[contador * cantidad_de_estaciones: contador * cantidad_de_estaciones + cantidad_de_estaciones])
    for contador in range(len(lista_red)):
        for mini_contador in range(len(lista_red[contador])):
            lista_red[contador][mini_contador] = int(lista_red[contador][mini_contador])
            
            
            
print(lista_red)




        contador = 2
        matriz_elevada = dcciudad.elevar_matriz(self.red, contador)
        estaciones_intermedias = contador -1
        
        if matriz_elevada[pos_estacion][pos_estacion] == 1:
            return estaciones_intermedias
        else:
            while matriz_elevada[pos_estacion][pos_estacion] == 0 and contador < len(self.red):
                contador += 1
                estaciones_intermedias = contador - 1
                matriz_elevada = dcciudad.elevar_matriz(self.red, contador)
        
        if matriz_elevada[pos_estacion][pos_estacion] == 1:
            return estaciones_intermedias