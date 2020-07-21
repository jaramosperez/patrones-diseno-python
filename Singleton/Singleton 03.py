"""

NOMBRE DE PATRON - SINGLETON
TIPO DE PATRON   - PATRON DE DISEÑO CREACIONAL.
"""
# Solution 03


class SingletonDecorator(object):
    def __init__(self, klass):
        self.klass = klass
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance == None:
            self.instance = self.klass(*args, **kwargs)
        return self.instance


@SingletonDecorator
class Logger(object):
    def __init__(self):
        self.start = None

    def write(self, message):
        if self.start:
            print(self.start, message)
        else:
            print(message)


logger_1 = Logger()
logger_1.start = "# >"
print("Logger 1", logger_1)
logger_1.write("Logger1 objeto es creado")
print(logger_1.start)

logger_2 = Logger()
logger_2.start = "$ >"
print("Logger 2", logger_2)
logger_1.write("Logger2 objeto es creado")
print(logger_1)
print(logger_2)
