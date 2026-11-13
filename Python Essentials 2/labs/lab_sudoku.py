# Una función que verifica si una lista contiene exactamente
# los nueve dígitos del 1 al 9.
def checkset(digs):
    # Convertir los elementos recibidos en una lista.
    digits = list(digs)
    # Ordenar los elementos de menor a mayor.
    digits = sorted(digits)
    # Crear una lista vacía para almacenar los dígitos esperados.
    expected = []
    # Recorrer los números del 1 al 9.
    for x in range(1, 10):
        # Obtener el código Unicode del carácter '0'.
        zero_code = ord('0')
        # Sumar el número actual al código Unicode de '0'.
        char_code = x + zero_code
        # Convertir el código Unicode en un carácter.
        character = chr(char_code)
        # Agregar el carácter a la lista esperada.
        expected.append(character)

    # Comparar ambas listas.
    # Si son iguales, significa que contiene todos los dígitos del 1 al 9.
    if digits == expected:
        return True
    else:
        return False


# Crear una lista vacía para almacenar las nueve filas del Sudoku.
rows = []
# Solicitar las nueve filas del Sudoku.
for r in range(9):
    # Variable para controlar si la fila ingresada es válida.
    ok = False
    # Repetir la solicitud mientras la fila no sea válida.
    while not ok:
        # Solicitar una fila al usuario.
        row = input("Ingresa fila #" + str(r + 1) + ": ")
        # Comprobar que tenga exactamente nueve caracteres
        # y que todos sean dígitos.
        if len(row) == 9 and row.isdigit():
            ok = True
        else:
            print("Datos de fila incorrectos: se requieren 9 dígitos")

    # Agregar la fila válida a la lista de filas.
    rows.append(row)


# Variable que determina si el Sudoku es correcto.
ok = True
# COMPROBAR LAS FILAS
# Recorrer todas las filas del Sudoku.
for r in range(9):
    # Comprobar si la fila contiene los dígitos del 1 al 9.
    if not checkset(rows[r]):
        # Si no es correcta, cambiar el estado de validación.
        ok = False
        # Interrumpir el ciclo porque ya encontramos un error.
        break

# COMPROBAR LAS COLUMNAS
# Realizar esta comprobación solamente si las filas son correctas.
if ok:
    # Recorrer las nueve columnas.
    for c in range(9):
        # Crear una lista vacía para almacenar una columna.
        col = []
        # Recorrer las nueve filas.
        for r in range(9):
            # Obtener el carácter de la fila actual
            # que corresponde a la columna actual.
            col.append(rows[r][c])
        # Comprobar si la columna contiene los dígitos del 1 al 9.
        if not checkset(col):
            # Si la columna no es correcta, marcar el Sudoku como inválido.
            ok = False
            # Interrumpir el ciclo.
            break

# COMPROBAR LOS SUBCUADRADOS DE 3x3
# Realizar esta comprobación solamente si las filas y columnas son correctas.
if ok:
    # Recorrer las filas iniciales de cada subcuadrado.
    # El salto de 3 permite visitar las posiciones 0, 3 y 6.
    for r in range(0, 9, 3):
        # Recorrer las columnas iniciales de cada subcuadrado.
        for c in range(0, 9, 3):
            # Crear una cadena vacía para almacenar el subcuadrado.
            sqr = ''
            # Recorrer las tres filas que forman el subcuadrado.
            for i in range(3):
                # Obtener tres caracteres consecutivos de la fila actual.
                # rows[r+i] selecciona la fila.
                # [c:c+3] selecciona tres caracteres desde la columna c.
                part = rows[r + i][c:c + 3]
                # Agregar esos tres caracteres a la cadena del subcuadrado.
                sqr = sqr + part
            # Convertir la cadena del subcuadrado en una lista.
            square_digits = list(sqr)
            # Comprobar si contiene los dígitos del 1 al 9.
            if not checkset(square_digits):
                # Si no es correcto, marcar el Sudoku como inválido.
                ok = False
                # Interrumpir el ciclo de los subcuadrados.
                break

# MOSTRAR EL RESULTADO FINAL
# Comprobar el estado de validación del Sudoku.
if ok:
    # Si todas las comprobaciones fueron correctas.
    print("Si")
else:
    # Si alguna comprobación encontró un error.
    print("No")