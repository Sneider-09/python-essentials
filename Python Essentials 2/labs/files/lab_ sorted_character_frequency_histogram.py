
from os import strerror

# Inicializa los contadores para las 26 letras
counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}

file_name = input("Ingresa el nombre del archivo a analizar: ")

try:
    with open(file_name, "rt") as file:
        for line in file:
            for char in line:
                char = char.lower()
                if char in counters:
                    counters[char] += 1

    # Ordenar de mayor a menor frecuencia usando lambda
    sorted_counters = sorted(
        counters.items(),
        key=lambda item: item[1],
        reverse=True
    )

    # Crear el archivo de salida
    with open(file_name + ".hist", "wt") as hist_file:
        for char, count in sorted_counters:
            if count > 0:
                hist_file.write(f"{char} -> {count}\n")
                print(f"{char} -> {count}")

except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))
