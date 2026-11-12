# La variante de un parámetro del método center() genera una copia 
# de la cadena original, tratando de centrarla dentro de un 
# campo de un ancho especificado.

# El centrado se realiza realmente al agregar algunos 
# espacios antes y después de la cadena.

# Demostración del método center():
print('[' + 'alpha'.center(10) + ']')

# Si la longitud del campo de destino es demasiado pequeña para 
# ajustarse a la cadena, se devuelve la cadena original.
print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')

# La variante de dos parámetros de center() hace uso del 
# carácter del segundo argumento, en lugar de un espacio.
print('[' + 'gamma'.center(20, '*') + ']')