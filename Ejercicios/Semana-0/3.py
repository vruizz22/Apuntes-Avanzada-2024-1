class Plato:
    def __init__(self, nombre: str, precio: int, nivel_picante: int, es_vegetariano: bool):
        self.nombre = nombre
        self.precio = precio
        self.nivel_picante = nivel_picante
        self.es_vegetariano = es_vegetariano

menu = [
    Plato("Pollo Tikka Masala", 8500, 3, False),
    Plato("Paneer Butter Masala", 9500, 2, True),
    Plato("Biryani de Cordero", 11500, 4, False),
    Plato("Samosas", 3500, 2, True),
    Plato("Dal Makhani", 7500, 1, True),
    Plato("Tandoori Chicken", 9000, 3, False),
    Plato("Chana Masala", 7500, 2, True),
    Plato("Rogan Josh", 10500, 4, False),
    Plato("Aloo Gobi", 6500, 2, True),
    Plato("Malai Kofta", 9500, 2, True)
]

if __name__ == "__main__":
    print("       Nombre        |  Precio  | Picante | Vegetariano")
    for plato in menu:
        picante = ("#" * plato.nivel_picante).center(7)
        vegetariano = "🌿" if plato.es_vegetariano else ""
        print(f"{plato.nombre:20} | {plato.precio:8} | {picante:7} | {vegetariano:11}")


