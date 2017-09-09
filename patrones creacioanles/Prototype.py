from copy import deepcopy
#sirve para crear clonaciones de objetos (instancias de clases)

#Metodo clonador
class Prototype(object):
    def clone(self):
        return deepcopy(self)


class ProductPrototype1(Prototype):
     def __init__(self):
        self.name = 'Beer'

class ProductPrototype2(Prototype):
    def __init__(self):
        self.name = 'Botana'

c1 = ProductPrototype1()
c2 = ProductPrototype2()
c1c = c1.clone()
c2c = c2.clone()
