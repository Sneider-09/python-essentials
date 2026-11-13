str_1 = input("Ingrese un texto: ").lower()
str_2 = input("Ingrese otro texto: ").lower()

# Quitar todos los espacios.
str_1 = str_1.replace(' ','')
str_2 = str_2.replace(' ','')

# Cambiar todas las letras a mayúsculas
str_1.upper()
str_2.upper()

# Convertirlas en listas
str_1 = list(str_1)
str_2 = list(str_2)

# Ordenar las listas
s_1 = sorted(str_1)
s_2 = sorted(str_2)

# Unir los elementos de cada lista en cadenas separadas
strx_1 = ''.join(s_1)
strx_2 = ''.join(s_2)

# Comparar las listas
if len(strx_1) > 0 and strx_1 == strx_2:
	print("Anagramas")
else:
	print("No son anagramas")