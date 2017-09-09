# represents the product created by the builder.
# puede ser utilizado cuando necesitemos crear objetos complejos
#compuestos de varias partes independientes
import abc

class Beer:
    def __init__(self):
        self.marca = None

    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def __str__(self):
        return "Cerveza [marca={0}]".format(self.marca)


# the builder abstraction
metaclass=None
class BeerBuilder(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def set_marca(self, marca):
        pass

    @abc.abstractmethod
    def get_result(self):
        pass

class BeerBuilderImpl(BeerBuilder):
    def __init__(self):
        self.beer = Beer()

    def set_marca(self, marca):
        self.beer.set_marca(marca)

    def get_result(self):
        return self.beer

#Construir una Cerveza Tecate
class BeerBuildDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.set_marca("Tecate");
        return self.builder.get_result()

if __name__ == '__main__':
    builder = BeerBuilderImpl()
    BeerBuildDirector = BeerBuildDirector(builder)
    #Mostrar la información de cada coche creado
    print(BeerBuildDirector.construct())
