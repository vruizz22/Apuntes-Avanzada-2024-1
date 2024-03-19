


archivo = open("correos.csv", "r")
data = archivo.readlines()
data = [line.rstrip('\n').split('\t') for line in data]
correos = [line[2] for line in data]
for correo in correos:
    print(correo)