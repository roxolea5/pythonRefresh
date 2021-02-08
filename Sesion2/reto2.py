"""
Haz un programa que funcione como un directorio de números telefonicos

Crea un diccionario que almacene números de telefono utilizando nombres como llaves, con al menos 5 números
Adquiere al menos uno de los números
Agrega nuevas entradas al diccionario

"""




directory = {
    'Rotz' : 3311331133,
    'Beatriz' : 3322332233,
    'Israel' : 3344334433,
    'Luisa' : 3355335533,
    'Moises' : 3355336633

}

print(directory)

print(directory.keys())
print(directory.values())

print(directory['Rotz'])

directory['Manuel'] = 3377337733

print(directory)

dpop = directory.pop('Manuel')

print(dpop) #Imprime el valor

print(directory)