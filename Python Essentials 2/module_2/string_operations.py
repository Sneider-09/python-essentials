# Sobrecarga
str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)

# Saber el valor del punto de código ASCII/UNICODE de un carácter específico
char_1 = 'a'
char_2 = ' '  # space

print(ord(char_1))
print(ord(char_2))

# Obtener el carácter correspondiente
print(chr(97))
print(chr(945))

# Nota
chr(ord("x")) == "x" # -> True
ord(chr(97)) == 97 # -> True

# Cadenas inmutables
alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet
alphabet = alphabet + "z"

print(alphabet)

# Encuentra el elemento mínimo de la secuencia pasada como argumento
# Demonstración de min() - Ejemplo 1:
print(min("aAbByYzZ"))


# Demonstración de min() - Ejemplos 2 y 3:
t = 'Los Caballeros Que Dicen "Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))

# Encuentra el elemento máximo de la secuencia.
# Demostración de max() - Ejemplo 1:
print(max("aAbByYzZ")) # -> z minúscula

# Demostración de max() - Ejemplo 2 y 3:
t = 'Los Caballeros Que Dicen "Ni!"'
print('[' + max(t) + ']') 

t = [0, 1, 2]
print(max(t)) 

# Busca la secuencia desde el principio, para encontrar el primer 
# elemento del valor especificado en su argumento.
# Demonstración del método index() method:
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

# Toma su argumento (una cadena) y crea una nueva lista que 
# contiene todos los caracteres de la cadena, uno por 
# elemento de la lista.
# Demostración de la función list():
print(list("abcabc"))

# Cuenta todas las apariciones del elemento dentro de la secuencia.
# Demostración del método count():
print("abcabc".count("b"))
print('abcabc'.count("d"))