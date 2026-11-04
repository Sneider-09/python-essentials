# Pregunta 1: ¿Cuál es la salida del siguiente fragmento de código? -> alt solo existe dentro de la función
def message():
    alt = 1
    print("¡Hola, mundo!")
 
print(alt)

# Pregunta 2: ¿Cuál es la salida del siguiente fragmento de código? -> 2 1
a = 1
  
def fun():
    a = 2
    print(a)
 
fun()
print(a)

# Pregunta 3: ¿Cuál es la salida del siguiente fragmento de código? -> 2 3
a = 1
 
def fun():
    global a
    a = 2
    print(a)
 
fun()
a = 3
print(a)

# Pregunta 4: ¿Cuál es la salida del siguiente fragmento de código? -> 2 2
a = 1
 
def fun():
    global a
    a = 2
    print(a)
 
a = 3
fun()
print(a)