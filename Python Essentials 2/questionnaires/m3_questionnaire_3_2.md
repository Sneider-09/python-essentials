**Pregunta 1: Suponiendo que hay una clase llamada Snakes, escribe la primera línea de la declaración de clase Python, expresando el hecho de que la nueva clase es en realidad una subclase de Snake.**
- class Python(Snakes):

**Pregunta 2: Algo falta en la siguiente declaración, ¿qué es?**
```
class Snakes:
    def __init__():
        self.sound = 'Sssssss'
```
- El parámetro self en el constructor

**Pregunta 3: Modifica el código para garantizar que la propiedad venomous sea privada.**
```
class Snakes:
    def __init__(self):
        self.venomous = True
```
- self.__venomous__ = True
