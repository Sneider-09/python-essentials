# Cifrado César - descifrando un mensaje.
cipher = input('Ingresa tu criptograma: ') # pide al usuario que ingrese un mensaje (cifrado) de una línea.
text = ''                                  # prepara una cadena para el mensaje descifrado (esta vacía por ahora)
for char in cipher:                        # inicia la iteración a través del mensaje.
    if not char.isalpha():                 # si el carácter actual no es alfabético...
        continue                           # ...ignorala.
    char = char.upper()                    # convierte la letra a mayúsculas
    code = ord(char) - 1                   # obtén el código de la letra y disminuyelo en uno.
    if code < ord('A'):                    # si es menor que el código de la Z...
        code = ord('Z')                    # ... cámbialo al código de la A.
    text += chr(code)                      # agrega el carácter recibido al final del mensaje descifrado.

print(text)                                # imprime el descifrado.