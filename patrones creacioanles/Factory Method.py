#El patron Factory Method o Metodo de Fabrica es una
#simplificacion del patron Abstract Factory.
#En un patron Factory Method solo existe un producto,
#no una familia de ellos.
class Botana(object):
    def __init__(self):
        self._price = None

    def get_price(self):
        return self._price

#Cada vez que se crea una botana nueva,
#deseariamos seleccionar el tipo de forma aleatoria
class CacahuatesBotana(Botana):
    def __init__(self):
        self._price = 15.0

class PapasBotana(Botana):
    def __init__(self):
        self._price = 20.0



class BotanaFactory(object):
    @staticmethod
    def create_botana(botana_type):
        if botana_type == 'Cacahuates':
            return CacahuatesBotana()
        elif botana_type == 'Papas':
            return PapasBotana()

if __name__ == '__main__':
    for botana_type in ('Cacahuates', 'Papas'):
          print('Price of {0} is {1}'.format(botana_type, BotanaFactory.create_botana(botana_type).get_price())
