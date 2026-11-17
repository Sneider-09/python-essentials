**Encuentra todos los métodos y atributos definidos. Localiza el contexto en el que existen: dentro del objeto o dentro de la clase.**
```
class Classy:
    varia = 1
    def __init__(self):
        self.var = 2

    def method(self):
        pass

    def __hidden(self):
        pass


obj = Classy()

print(obj.__dict__)
print(Classy.__dict__)
```

**__name__ contiene el nombre de la clase. No es nada emocionante, es solo una cadena.**
```
class Classy:
    pass


print(Classy.__name__)
obj = Classy()
print(type(obj).__name__) 
```

**__module__ es una cadena, también almacena el nombre del módulo que contiene la definición de la clase.**
```
class Classy:
    pass


print(Classy.__module__)
obj = Classy()
print(obj.__module__)      
```

**___bases__ es una tupla. La tupla contiene clases (no nombres de clases) que son superclases directas de la clase.**
```
class SuperOne:
    pass


class SuperTwo:
    pass


class Sub(SuperOne, SuperTwo):
    pass


def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)
 
```

**Introspección,** que es la capacidad de un programa para examinar el tipo o las propiedades de un objeto en tiempo de ejecución.
**Reflexión,** que va un paso más allá, y es la capacidad de un programa para manipular los valores, propiedades y/o funciones de un objeto en tiempo de ejecución.