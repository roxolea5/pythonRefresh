i = 1
while i <= 5:
    print(i)
    i += 1
print("Programa terminado")

for i in range (5):
    print(i)
print("Fin del ciclo")

# los ciclos for nos permiten recorrer estructuras de datos iterables Por ejemplo listas
animales = ['gato', 'perro', 'serpiente']
for animal in animales:
    print ("El animal es: {}, tamaño de palabra es: {}".format(animal, len(animal)))

#Para diccionarios podemos obtener las llaves y valores y luego recorrerlos

d3 = {"Usuario": "usser123", "Correo": "us12@bedu.org", "Compañia": "Bedu"} 

cantidad_datos = d3.items()

for campo, valor in cantidad_datos:
    print("el campo {} contiene: {}".format(campo, valor))