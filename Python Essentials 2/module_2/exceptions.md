## Excepciones
```
value = 1
value /= 0
```

- Este error de excepción es llamado ZeroDivisionError.
```
Traceback (most recent call last):
File "div.py", line 2, in <module>
value /= 0
ZeroDivisionError: division by zero
```

- La palabra reservada try comienza con un bloque de código el cual puede o no estar funcionando correctamente.
- Después, Python intenta realizar la acción arriesgada: si falla, se genera una excepción y Python comienza a buscar una solución.
- La palabra reservada except comienza con un bloque de código que será ejecutado si algo dentro del bloque try sale mal: si se genera una excepción dentro del bloque anterior try, fallará aquí, entonces el código ubicado después de la palabra clave reservada except debería proporcionar una reacción adecuada a la excepción generada.
- Por ultimo, se regresa al nivel de anidación anterior, es decir, se termina la sección try-except.

```
first_number = int(input("Ingresa el primer número: "))
second_number = int(input("Ingresa el segundo numero: "))

try:
    print(first_number / second_number)
except:
    print("Esta operación no puede ser realizada.")

print("FIN.")
```

**Emplear una variante más avanzada de la instrucción**
```
try:
    :
except exc1:
    :
except exc2:
    :
except:
    :
```

- Si el try genera la excepción exc1, esta será manejada por el bloque except exc1:.
- De la misma manera, si el try genera la excepción exc2, esta será manejada por el bloque except exc2:.
- Si el try genera cualquier otra excepción, será manejado por el bloque sin nombre except.

```
try:
    x = int(input("Ingresa un número: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("No puedes dividir entre cero, lo siento.")
except ValueError:
    print("Debes ingresar un valor entero..")
except:
    print("Oh cielos, algo salió mal...")

print("FIN.")
```