from math import sin, pi

print(sin(pi/2))

# Reemplazan las definiciones originales (importadas) dentro del namespace del código.
pi = 3.14

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

print(sin(pi / 2))

# Se ha invertido la secuencia de las operaciones del código
from math import sin, pi

print(sin(pi / 2))