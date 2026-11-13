# Cifrado César.
text = input("Ingresa tu mensaje: ") # pide al usuario que ingrese un mensaje (sin cifrar) de una línea.
cipher = ''                          # prepara una cadena para el mensaje cifrado (esta vacía por ahora).
for char in text:                    # inicia la iteración a través del mensaje.
    if not char.isalpha():           # si el carácter actual no es alfabético...
        continue                     # ...ignorala.
    char = char.upper()              # convierte la letra a mayúsculas
    code = ord(char) + 1             # obtén el código de la letra e increméntalo en uno.
    if code > ord('Z'):              # si es mayor que el código de la Z...
        code = ord('A')              # ... cámbialo al código de la A.
    cipher += chr(code)              # agrega el carácter recibido al final del mensaje cifrado.

print(cipher)                        # imprime el cifrado.
    