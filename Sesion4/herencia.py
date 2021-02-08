class Mascota:

    def __init__(self, nombre, tipo):
        self.nombre = nombre
    
    def moverse(self):
        pass
        
    def hace_ruido(self):
        pass

class Perro(Mascota):
    """Declaración de clase Perr"""
    def __init__(self, nombre):
        super().__init__(nombre, 'perro')

    def moverse(self):
        print('{} está corriendo en el patio'.format(self.nombre))
        
    def hace_ruido(self):
        print('{} está diciendo "guau"'.format(self.nombre))

class Gato(Mascota):
    """Declaración de clase Perr"""
    def __init__(self, nombre):
        super().__init__(nombre, 'gato')

    def moverse(self):
        print('{} está corriendo en la azotea'.format(self.nombre))
        
    def hace_ruido(self):
        print('{} está diciendo "miau"'.format(self.nombre))

class Cuyo(Mascota):
    """Declaración de clase Perr"""
    def __init__(self, nombre):
        super().__init__(nombre, 'cuyo')

    def moverse(self):
        print('{} está corriendo su jaula'.format(self.nombre))
        
    def hace_ruido(self):
        print('{} está diciendo "cui"'.format(self.nombre))

astro = Perro('astro')
astro.moverse()
astro.hace_ruido()
tommy = Gato('tommy')
tommy.moverse()
tommy.hace_ruido()
cuyito = Cuyo('cuyito')
cuyito.moverse()
cuyito.hace_ruido()
