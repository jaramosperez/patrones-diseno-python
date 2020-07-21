"""
Nombre del Patron - Singleton
Tipo de Patron    - Patron de Diseño Creacional.

"""

# Solucion 01
#Creamos nuestra clase Singleton
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

#Creacmos una instancia de Singleton y le pasamos un nombre
objeto_01 = Singleton()
print('Objeto 01 == >', objeto_01)
objeto_01.nombre = "Claudia"

#Creamos una 'nueva' instancia de Singleton y le pasamos un nombre
objeto_02 = Singleton()
print('Objeto 02 ==> ', objeto_02)
print('Objeto 02 nombre ==>', objeto_02.nombre)
objeto_02.nombre = "Yanina"

# Al Utilizar este patron de dieño siempre que instanciemos esta clase, siempre será el mismo objeto.
print('Objeto 01 nombre ==> ', objeto_01.nombre)
print('Objeto 02 nombre ==> ', objeto_02.nombre)