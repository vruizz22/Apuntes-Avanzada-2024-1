lista_original = [ [1,2], [3,4] ]
copia = [[int(numero) for numero in sublista] for sublista in lista_original]
copia[0][0] = 9
print(lista_original)