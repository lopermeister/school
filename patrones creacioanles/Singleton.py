#el patron Singleton se utiliza para no permitir que existan multiples instancias de una clase,
#sino solamente una.
class MySingleton(object):
     INSTANCE = None

     def __init__(self):
        if self.INSTANCE is not None:
            raise ValueError("An instantiation already exists!")
        # do your init stuff

     @classmethod
     def get_instance(cls):
        if cls.INSTANCE is None:
             cls.INSTANCE = MySingleton()
        return cls.INSTANCE
