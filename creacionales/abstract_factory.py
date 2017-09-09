#"""PDD-PATRONES CREACIONALES-ABSTRACTFACTORY"""
import random

class Restaurant:
    def _init_(self,Hamburguesa_factory=None):
        self.burger_factory = Hamburguesa_factory

    def show_platillo(self):
        burger = self.burger_factory.get_burger()
        print "Esta es una hamburguesa", burger
        print "contiene", burger.ingredientes()

class hamburguesa_sencilla():
    def ingredientes(self):
        return "pan\nlechuga\ncarne de res\ntomate\nqueso jack\n"
    def _str_(self):
        return "hamburguesa sencilla"

class hamburguesa_especial():
    def ingredientes(self):
        return "pan\nlechuga\ntomate\nribeye\nqueso jack\ntocino\n"
    def _str_(self):
        return "hamburguesa especial"

class SencillaFactory:
    def get_burger(self):
        return hamburguesa_sencilla()

class EspecialFactory:
    def get_burger(self):
        return hamburguesa_especial()

def get_factory():
    return random.choice([SencillaFactory,EspecialFactory])()

foodStand=Restaurant()
for i in range (3):
    foodStand.burger_factory = get_factory()
    foodStand.show_platillo()
    print "=" * 10
