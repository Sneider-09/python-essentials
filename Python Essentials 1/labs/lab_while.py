blocks = int(input("Ingresa el número de bloques: "))

#
# Escribe tu código aquí.
height = 0
count = 1
while count <= blocks:
  blocks -= count
  height += 1
  count += 1
#


print("La altura de la pirámide:", height)

