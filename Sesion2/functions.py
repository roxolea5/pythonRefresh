def hola_mundo():
    print("Hola Mundo")
#Para llamarlas, lo hacemos por su nombre
hola_mundo()

def saludo(persona):
    print("Hola {}".format(persona))

saludo("Luis")
saludo("Bedu")
saludo("Mundo")

def area_rectangulo(base, altura):
    area = base * altura
    return area

b = 5
h = 3
area = area_rectangulo(b, h)

print(area)