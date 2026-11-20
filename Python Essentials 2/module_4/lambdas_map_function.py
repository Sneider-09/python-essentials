# Se construye la list_1 con valores del 0 al 4.
list_1 = [x for x in range(5)]
# Crear una nueva lista en la que todos los elementos han sido
# evaluados como 2 elevado a la potencia tomada del elemento 
# correspondiente de list_1
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)
# la segunda lambda aquí - solo eleva al cuadrado cada elemento de list_2
for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()