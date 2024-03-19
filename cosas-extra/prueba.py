
archivo = open("texto.txt", "r")
data = archivo.readlines()
info = [line.rstrip('\n') for line in data]
print(info)
numeros = info[-1].split(",")
print(numeros)
lista_red = []
cantidad_de_estaciones = int(info[0])
for contador in range(cantidad_de_estaciones):
    lista_red.append(numeros[contador: contador + cantidad_de_estaciones])
for contador in range(len(lista_red)):
    for mini_contador in range(len(lista_red[contador])):
        lista_red[contador][mini_contador] = int(lista_red[contador][mini_contador])
print(lista_red)