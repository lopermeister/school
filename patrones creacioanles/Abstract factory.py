import random

class Bar:
    "Cervezas"
    #resuelve el problema de crear familias de objetos

    def __init__(self, Cerveza_factory=None):
        self.beer_factory=Cerveza_factory

    def que_cerveza(self):
        beer=self.beer_factory.get_beer()
        print "This is a beer ", beer
        print "It be", beer.tem()

#tenemos 2 Cervezas diferentes: una clara y otra oscura
class Clara():

    def tem(self):
        return "cool"
    def __str__(self):
        return "Clara"
class Obscura():

    def tem(self):
        return "hot"
    def __str__(self):
        return "Obscura"

# Clases de fabrica
class ClaraFactory:
    def get_beer(self):
        return Clara()

class ObscuraFactory:
    def get_beer(self):
        return Obscura()

# Crear la familia fabrica
#En este patrón se crean ciertas clases adicionales llamadas
#fábricas. Estas clases son las encargadas de crear los diferentes tipos objetos

def get_factory():
    """Let's be dynamic!"""
    return random.choice([ClaraFactory, ObscuraFactory])()

b=Bar()
for i in range(3):
    b.beer_factory = get_factory()
    b.que_cerveza()
    print "=" *15
