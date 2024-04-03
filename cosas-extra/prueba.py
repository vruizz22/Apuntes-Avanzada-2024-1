class Variable:
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, x):
        print(f"valor: {self.valor}")
        print(f"x: {x}")
        if x <= 0:
            print("negativo")
            self._valor = x
        else:
            print("positivo")
            self._valor = -x

variable_uno = Variable(5)
print("Entre")
# Paso 1
variable_uno.valor -= 3 # 2
print("Calcule")
print(variable_uno.valor) # -2
print()
print("Paso 2")
# Paso 2
variable_uno.valor = -1 # Aqui variable._uno.valor se le asigna -1, 
print("Esto es",)
print("Calcule")
print(variable_uno.valor)
print()
print("Paso 3")
# Paso 3
variable_uno.valor += 3
print("Calcule")
print(variable_uno.valor)