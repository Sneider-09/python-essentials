from platform import platform, machine, processor, system, version, python_implementation, python_version_tuple

# La función platform

# platform(aliased = False, terse = False)

# aliased → cuando se establece a True (o cualquier valor distinto a cero) 
# puede hacer que la función presente los nombres de capa subyacentes alternativos 
# en lugar de los comunes.

# terse → cuando se establece a True (o cualquier valor distinto a cero) 
# puede convencer a la función de presentar una forma más breve del resultado 
# (si lo fuera posible).

print(platform())
print(platform(1))
print(platform(0, 1))

# La función machine
print(machine())

# La función processor
print(processor())

# La función system
print(system())

# La función version
print(version())

# Las funciones python_implementation y python_version_tuple

# python_implementation() → devuelve una cadena que denota la implementación 
# de Python (espera CPython aquí, a menos que decidas utilizar cualquier rama 
# de Python no canónica).

# python_version_tuple() → devuelve una tupla de tres elementos la cual contiene:
#  La parte mayor de la versión de Python.
#  La parte menor.
#  El número del nivel de parche.

print(python_implementation())

for atr in python_version_tuple():
    print(atr)