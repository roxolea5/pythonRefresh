print ("Hola mundo")

#tipos de dato numéricos
entero = 4
print("El dato introducido contiene:")
print(entero)
print("Es de tipo:")
print(type(entero))


pi = 3.14159
print("El dato introducido contiene:")
print(pi)
print("Es de tipo:")
print(type(pi))

#Cadenas de texto
mensaje = "Hola Mundo"
print("El dato introducido contiene:")
print(mensaje)
print("Es de tipo:")
print(type(mensaje))

#Datos booleanos
verdadero = True
print("El dato introducido contiene:")
print(verdadero)
print("Es de tipo:")
print(type(verdadero))

#Se puede definir números como cadenas si se encierran en comillas
numero1 = "100"
numero2 = "3.14159"
print(type(numero1))

#Para convertir a entero 
entero = int(numero1)
print(type(entero))

#Para convertir a flotante
flotante = float(numero2)
print(type(flotante))

#También se puede convertir un número a cadena de texto
num = 300
cadena = str(num)
print(type(cadena))

"""
Reto 1:

Utilizando 3 variables:
    1. Texto
    2. Nombre
    3. Frase

    Hola mi nombre es (nombre) y mi frase favorita es (frase)
"""

nombre = "Roxana"
frase = "'el eterno momento presente'"
texto = "Hola mi nombre es {} y mi frase favorita es {}".format(nombre, frase)

print (texto)
print ("Hola mi nombre es", nombre, "y mi frase favorita es", frase)
print ("Hola mi nombre es " + nombre+ " y mi frase favorita es "+ frase)











