text = input("Ingrese un texto")

# Quitar todos los espacios...
text = text.replace(' ','')

# Revisar si la palabra es igual en ambos sentidos
if len(text) > 1 and text.upper() == text[::-1].upper():
	print("Es un palíndromo")
else:
	print("No es un palíndromo")
