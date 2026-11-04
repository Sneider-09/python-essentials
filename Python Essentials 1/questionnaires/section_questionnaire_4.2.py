# Pregunta 1: ¿Cuál es la salida del siguiente fragmento de código? -> Mi nombre es Bond. James Bond.
def intro(a="James Bond", b="Bond"):
     print("Mi nombre es", b + ".", a + ".")
 
intro()

# Pregunta 2: ¿Cuál es la salida del siguiente fragmento de código? -> Mi nombre es Sean Connery. James Bond.
def intro(a="James Bond", b="Bond"):
    print("Mi nombre es", b + ".", a + ".")
 
intro(b="Sean Connery")

# Pregunta 3: ¿Cuál es la salida del siguiente fragmento de código? -> Mi nombre es Bond. Susan.
def intro(a, b="Bond"):
    print("Mi nombre es", b + ".", a + ".")
 
intro("Susan")

# Pregunta 4: ¿Cuál es la salida del siguiente fragmento de código? -> Primero deben ir los parámetros posicionales
def add_numbers(a, b=2, c):
    print(a + b + c)
 
add_numbers(a=1, c=3)
 