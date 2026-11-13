## Hay al menos dos formas posibles de que "salga mal" la ejecución.
```
import math

x = float(input("Ingresa x: "))
y = math.sqrt(x)

print("La raíz cuadrada de", x, "es igual a", y)
```

- Como el usuario puede ingresar una cadena de caracteres completamente arbitraria, no hay garantía de que la cadena se pueda convertir en un valor flotante: esta es la primera vulnerabilidad del código.

```
Ingresa x: Abracadabra
 
Traceback (most recent call last):
 
  File "sqrt.py", line 3, in <module>
 
    x = float(input("Ingresa x: "))
 
ValueError: could not convert string to float: 'Abracadabra'
```

- La segunda es que la función sqrt() fallará si se le ingresa un valor negativo.
```
Enter x: -1
 
Traceback (most recent call last):
 
  File "sqrt.py", line 4, in <module>
 
    y = math.sqrt(x)
 
ValueError: math domain error
```