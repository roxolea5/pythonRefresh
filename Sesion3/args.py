def sumatoria(*mis_parametros):
    suma = 0;
    for numero in mis_parametros:
        suma += numero
    return suma

resultado = sumatoria(1,2,3,4,5)
print(resultado)

def crear_usuario(**parametros_extra):
    user = {
        'email': 'roxana@gmail.com',
        'password' : 'hjdsjsfjfs'
    }

    for llave in parametros_extra:
        user[llave] = parametros_extra[llave]

    print(user)



crear_usuario(birthday = '05/09/1990', language='español')

def hola (email, password, *args, **kwargs):
    print(email, password)
    print(args)
    print(kwargs)

hola ('Rotz', 'jhhjk', 1,2,3,4,5, nombre='Roxana')