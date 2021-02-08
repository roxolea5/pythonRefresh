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