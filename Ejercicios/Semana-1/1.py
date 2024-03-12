class Alumno:
    
    def __init__(self, nombre, apellido, numero_alumno):
        self.nombre = nombre
        self.apellido = apellido
        self.numero_alumno = numero_alumno
        self.clases_asistidas = []
    
class Sala:
    
    def __init__(self, lista_alumnos, numero_sala, sigla):
        self.lista_alumnos = lista_alumnos
        self.numero_sala = numero_sala
        self.sigla = sigla

    
    def ingresar_alumno(self, alumno):
        if alumno.numero_alumno in [alumno[1] for alumno in self.lista_alumnos] and alumno.nombre in [alumno[0] for alumno in self.lista_alumnos]:
            print("{} {} ha ingresado a la Sala {} - {}".format(alumno.nombre, alumno.apellido, self.numero_sala, self.sigla))
        else:
            print("{} {} se ha intentado colar a la Sala {} - {}".format(alumno.nombre, alumno.apellido, self.numero_sala, self.sigla))
        
if __name__ == "__main__":
    javier = Alumno("Javier", "Gomez", "18639942")
    josefa = Alumno("Josefa", "Paz", "16645578")
    tomas = Alumno("Tomas", "Gonzalez", "19638225")

    sala = Sala([("Michael", "19643721"),("Silvana", "18632890"),("Tomas", "19638225"),
                 ("Josefa", "16645578"),("Javier", "16665798"),("", "")], 666, "IIC2233")
    sala.ingresar_alumno(javier)
    sala.ingresar_alumno(josefa)
    sala.ingresar_alumno(tomas)