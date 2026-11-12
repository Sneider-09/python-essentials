# El método capitalize() hace exactamente lo que dice, crea una nueva cadena con 
# los caracteres tomados de la cadena fuente, pero intenta modificarlos de la 
# siguiente manera:

# Si el primer carácter dentro de la cadena es una letra (nota: el primer 
# carácter es el elemento con un índice igual a 0, no es el primer 
# carácter visible), se convertirá a mayúsculas.

# Todas las letras restantes de la cadena se convertirán a minúsculas.

# Demostración del método capitalize():
print('aBcD'.capitalize())
print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())