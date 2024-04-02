from math import ceil


class SitioWeb:

    def __init__(self, url, mail, ip):
        self.url = url
        self.mail = mail
        self.ip = ip
        self.reclamos = []

    def recibir_reclamo(self, mail_usuario, texto):
        self.reclamos.append([mail_usuario, texto])


class DCChrome:
    def __init__(self, mail):
        self.mail = mail
        self.sitios = []
        self.back_stack = []
        self.forward_stack = []

    def cargar_paginas(self, nombre_archivo):
        with open(nombre_archivo) as archivo:
            primera_linea = archivo.readline().strip().split(",")
            for linea in archivo:
                datos_sitio = linea.strip().split(",")
                dic_sitio_web = {"url": datos_sitio[0], "ip": datos_sitio[1], "mail": datos_sitio[2]}
                self.sitios.append(SitioWeb(**dic_sitio_web))
                
    def listado_de_sitios(self, sitio_anterior=-1):
        index = 0
        while True:
            sitio_2 = ""
            sitio_3 = ""
            if index + 1 < len(self.sitios):
                sitio_2 = self.sitios[index + 1].url
            if index + 2 < len(self.sitios):
                sitio_3 = self.sitios[index + 2].url
            print("Listado de sitios")
            print("-" * 62)
            print(f"{self.sitios[index].url:^20.20s}|{sitio_2:^20.20s}|{sitio_3:^20.20s}")
            print(f"{1: ^20d}|{2: ^20d}|{3: ^20d}")
            print("-" * 62)
            print("1. Sitio 1")
            print("2. Sitio 2")
            print("3. Sitio 3")
            print("4. ->")
            print("5. <-")
            print("6. Salir")
            
            if sitio_anterior != -1:
                print("7. Volver al sitio")
            nro = input("Elija una opción: ")
            print()

            if nro == 1:
                if self.back_stack:
                    nuevo_sitio = self.back_stack.pop()
                    self.forward_stack.append(nuevo_sitio)
                    self.entrar_a_sitio()
                    break
            
            if nro == "7" and sitio_anterior != -1:
                self.back_stack.pop()
                self.entrar_a_sitio(sitio_anterior)
                break

    def entrar_a_sitio(self, nro_sitio):
        while True:
            print(f"{self.sitios[nro_sitio].url:^62s}")
            print(f"{self.sitios[nro_sitio].ip:^62s}")
            print(f"{self.sitios[nro_sitio].mail:^62s}")
            print("-" * 62)
            print("Reclamos:")
            print()
            for mail_user, reclamo in self.sitios[nro_sitio].reclamos:
                print(f"from: {mail_user}")
                print(f"to: {self.sitios[nro_sitio].mail}")
                for i in range(ceil(len(reclamo) / 62)):
                    print(f"{reclamo[62 * i: 62 * (i + 1)]:62s}")
                print()
            print("-" * 62)
            sitio_atras = ""
            sitio_adelante = ""
            if self.back_stack:
                sitio_atras = self.sitios[self.back_stack[-1]].url
            if self.forward_stack:
                sitio_adelante = self.sitios[self.forward_stack[-1]].url
            print(f"1. Atrás: {sitio_atras}")
            print(f"2. Adelante: {sitio_adelante}")
            print("3. Escribir reclamo")
            print("4. Listado de sitios")
            print("5. Salir")
            nro = input("Elija una opción: ")
            print()
            
            # COMPLETAR
        
            
            if nro == "3":
                reclamo = input("Escriba su reclamo: ")
                self.sitios[nro_sitio].reclamos.append([self.mail, reclamo])
            if nro == "4":
                self.back_stack.append(nro_sitio)
                self.listado_de_sitios(nro_sitio)
                break
            if nro == "5":
                break


# descomentar la última línea cuando esté listo

navegador = DCChrome("tu.mail@uc.cl")
navegador.cargar_paginas("data.csv")
# navegador.listado_de_sitios()