my_tuple = (1,2)
one_tuple = (1,)

# Creando una tupla vacia
t1 = ()
t2 = tuple()


# Tupla de un elemento

t3 = (1, )  # Sin la coma no se detecta como tupla

# Asignacion multiple con tupla

a, b = (10, 20)

print(a)
print(type(t1))

print(b) 

#No se puede modificar una tupla, quitar comentarios para comprobar

#t1.insert(0, 1)
#t1.append(10)

print(t1)

a = t3[0]

l1 = list(t3)

print(l1)
print(t3)