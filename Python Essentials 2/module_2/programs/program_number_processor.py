#Procesador de Números.
line = input("Ingresa una línea de números, sepáralos con espacios: ")  # pide al usuario que ingrese una línea llena de cualquier cantidad de números
strings = line.split()                                                  # divide la línea en una lista con subcadenas
total = 0                                                               # se inicializa la suma total a cero
try:                                                                    # la conversión de cadena a flotante puede generar una excepción
    for substr in strings:                                              # itera a través de la lista...
        total += float(substr)                                          # ...intenta convertir todos sus elementos en números flotantes; si funciona, aumenta la suma.
    print("El total es:", total)                                        # imprime la suma
except:                                                                 # el programa termina aquí en caso de error
    print(substr, "no es un numero.")                                   # imprime un mensaje de diagnóstico