**Pregunta 1: La declaración de la clase Snake se muestra a continuación. Enriquece la clase con un método llamado increment(), el cual incrementa en 1 la propiedad victims.**
```
class Snake:
    def __init__(self):
        self.victims = 0
    def increment(self):
        self.victims += 1
```
- Respuesta: 
```
def increment(self):
    self.victims += 1
```

**Pregunta 2: Redefine el constructor de la clase Snake para que tenga un parámetro que inicialice el campo victims con un valor pasado al objeto durante la construcción.**
- Respuesta:
```
def __init__(self, val):
        self.victims = val
```

**Pregunta 3: ¿Puedes predecir el resultado del siguiente código?**
```
class Snake:
    pass
 
 
class Python(Snake):
    pass
 
 
print(Python.__name__, 'es una', Snake.__name__)
print(Python.__bases__[0].__name__, 'puede ser una', Python.__name__)
```
- Python es una Snake
- Snake puede ser una Python