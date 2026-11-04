# Pregunta 1: ¿Cuál es la salida del siguiente programa si el usuario ingresa un 0? -> Entrada errónea...
try:
    value = int(input("Ingresa un número entero: "))
    print(value/value)
except ValueError:
    print("Entrada incorrecta...")
except ZeroDivisionError:
    print("Entrada errónea...")
except:
    print("¡Buuuu!")
 
# Pregunta 2: ¿Cuál es la salida del siguiente programa si el usuario ingresa un 0? -> TypeError
value = input("Ingresa un número entero: ")
print(10/value)