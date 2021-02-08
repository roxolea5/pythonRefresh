class Pila:

    def __init__(self):
        self.stack = list()

    def push(self, elemento):
        self.stack.append(elemento)
        print("Elemento '{}' añadido".format(elemento))
        print (self.stack)

    def pop(self):
        if not self.stack:
            print("Pila vacía")
        else:
            print ("Se ha eliminado el elemento '{}'".format(self.stack[-1]))
            retirado = self.stack[-1]
            self.stack.pop()
            return retirado

    def peek(self):
        if not self.stack:
            print("Pila vacía")
        else:
            print('El último elemento de la pila es "{}"'.format(self.stack[-1]))
            ultimo = self.stack[-1]
            return ultimo

    def __str__(self):
        return str(self.stack)

mi_pila = Pila()



mi_pila.push('elefante')
mi_pila.push('conejo')
mi_pila.push('gato')

deleted = mi_pila.pop()
print (deleted)
otro_elemento = mi_pila.peek()
print (otro_elemento)
print(mi_pila)

"""
mi_pila.quitar()
mi_pila.agregar('Hola')
mi_pila.agregar('intento')
mi_pila.peek()
#print(mi_pila)


"""