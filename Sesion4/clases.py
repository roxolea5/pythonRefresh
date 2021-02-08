class Mascota:

    def __init__(self, nombre, tipo, color):
        self.nombre = nombre
        self.tipo = tipo
        self.color = color
    
    def moverse(self):
        if self.tipo == 'serpiente':
            print ('{} está reptando'.format(self.nombre ))
        else:
            print ('{} está corriendo'.format(self.nombre))

    def hace_ruido(self):
        if self.tipo == 'serpiente':
            print ('La {} {} está seseando'.format(self.tipo, self.color))
        elif self.tipo == 'perro':
            print ('El {} {} está ladrando'.format(self.tipo, self.color))
        else:
            print ('El {} {} está maullando'.format(self.tipo, self.color))

    
        


snake = Mascota('Ka', 'serpiente', 'roja')
snake.moverse()
snake.hace_ruido()

tom = Mascota('Tom', 'gato', 'gris')
tom.moverse()
tom.hace_ruido()

snoopy = Mascota('Snoopy', 'perro', 'blanco')
snoopy.moverse()
snoopy.hace_ruido()

