class Pila:

    def __init__(self):
        self.stack = list()

    def agregar(self, elemento):
        self.stack.append(elemento)
        print("Elemento '{}' añadido".format(elemento))
        print ("", self.stack)

    def quitar(self):
        if not self.stack:
            print("Pila vacía")
        else:
            print ("Se ha eliminado el elemento '{}'".format(self.stack[-1]))
            self.stack.pop()

    def peek(self):
        if not self.stack:
            print("Pila vacía")
        else:
            print('El último elemento de la pila es "{}"'.format(self.stack[-1]))

    def __str__(self):
        print(' ', self.stack)

mi_pila = Pila()


"""
mi_pila.agregar('Hola')
mi_pila.agregar('intento')
mi_pila.agregar('ser')
mi_pila.agregar('una')
mi_pila.agregar('pila')
mi_pila.peek()
mi_pila.quitar()

"""
mi_pila.quitar()
mi_pila.agregar('Hola')
mi_pila.agregar('intento')
mi_pila.peek()
mi_pila.quitar()
mi_pila.quitar()
mi_pila.peek()




        
