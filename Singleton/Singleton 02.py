"""
Método 02 Monostate(Borg) Pattern
Esta solución la propuso Alex Martelli
La llamo Monostate(Borg)

TIPO DE PATRON - PATRON DE DISEÑO CREACIONAL.

"""


class Borg(object):
    _shared = {}

    def __init__(self):
        self.__dict__ = self._shared
        # Todas las propiedades son almacenadas en la variable __dic__


class Singleton(Borg):
    def __init__(self, arg):
        Borg.__init__(self)
        self.val = arg


persona_01 = Singleton("Javier")
print("Objeto - 1 ==> ", persona_01)
print("Objeto - 1 val ==>", persona_01.val)

persona_02 = Singleton("Alejandro")
print("Objeto - 2 ==>", persona_01)
print("Objeto - 2 val ==> ", persona_01.val)
print("Objeto - 1 val ==> ", persona_02.val)

