from os import strerror

# solicitan al usuario el nombre del archivo a copiar e intentan abrirlo 
# para leerlo; se termina la ejecución del programa si falla la apertura
srcname = input("Ingresa el nombre del archivo fuente: ")
try:
    src = open(srcname, 'rb')
except IOError as e:
    print("No se puede abrir archivo fuente: ", strerror(e.errno))
    exit(e.errno)	

# repiten casi la misma acción, pero esta vez para el archivo de salida.
dstname = input("Ingresa el nombre del archivo destino: ")
try:
    dst = open(dstname, 'wb')
except Exception as e:
    print("No se puede crear el archivo de destino: ", strerror(e.errno))
    src.close()
    exit(e.errno)	

# prepara una parte de memoria para transferir datos del archivo fuente 
# al destino; tal área de transferencia a menudo se llama un búfer
buffer = bytearray(65536)
# cuenta los bytes copiados: este es el contador y su valor inicial
total  = 0
try:
    # intenta llenar el búfer por primera vez.
    readin = src.readinto(buffer)
    # mientras se obtenga un número de bytes distinto a cero, repite las mismas acciones
    while readin > 0:
        # escribe el contenido del búfer en el archivo de salida
        written = dst.write(buffer[:readin])
        # actualiza el contador
        total += written
        # lee el siguiente fragmento de archivo
        readin = src.readinto(buffer)
except IOError as e:
    print("No se puede crear el archivo de destino: ", strerror(e.errno))
    exit(e.errno)	

# limpieza final, el trabajo está hecho
print(total,'byte(s) escritos con éxito')
src.close()
dst.close()
    