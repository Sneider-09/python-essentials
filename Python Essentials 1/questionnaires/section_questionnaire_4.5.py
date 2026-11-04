# Pregunta 1: ¿Qué ocurrirá al intentar ejecutar el siguiente fragmento de código y por qué? -> La función no tiene una condición de terminación 
def factorial(n):
    return n * factorial(n - 1)
 
 
print(factorial(4))

# Pregunta 2: ¿Cuál es la salida del siguiente fragmento de código? -> 56
def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)
 
 
print(fun(25))