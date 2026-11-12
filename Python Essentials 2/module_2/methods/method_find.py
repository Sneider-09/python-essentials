# El método find() es similar al método index(), el cual ya conoces, 
# busca una subcadena y devuelve el índice de la primera aparición 
# de esta subcadena, pero:

# Es más seguro, no genera un error para un argumento que contiene 
# una subcadena inexistente (devuelve -1 en dicho caso).

# Funciona solo con cadenas, no intentes aplicarlo a ninguna otra 
# secuencia.

# Demostración del método find():
print("Eta".find("ta"))
print("Eta".find("mma"))

# Nota: no se debe de emplear find() si deseas verificar si un 
# solo carácter aparece dentro de una cadena, el operador in 
# será significativamente más rápido.
t = 'theta'
print(t.find('eta')) #-> 2
print(t.find('et')) #-> 2
print(t.find('the')) #-> 0
print(t.find('ha')) #-> -1 

# Si deseas realizar la búsqueda, no desde el principio de la 
# cadena, sino desde cualquier posición, puedes usar una variante 
# de dos parámetros
print('kappa'.find('a', 2)) #-> 4

# Se puede emplear el método find() para buscar todas las 
# ocurrencias de la subcadena, como aquí:
the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)
    
# El tercer argumento apunta al primer índice que no se tendrá 
# en cuenta durante la búsqueda (en realidad es el límite superior 
# de la búsqueda).
print('kappa'.find('a', 1, 4)) #-> 1
print('kappa'.find('a', 2, 4)) #-> -1
