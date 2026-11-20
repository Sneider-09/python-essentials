from os import strerror

# Ejemplo 1
stream = open("text.txt")
print(stream.readlines(20))
print(stream.readlines(20))
print(stream.readlines(20))
print(stream.readlines(20))
stream.close()

# Ejemplo 2
try:
    ccnt = lcnt = 0
    s = open('text.txt', 'rt')
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print("\n\nCaracteres en el archivo:", ccnt)
    print("Líneas en archivo:     ", lcnt)
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))
    
# Ejemplo 3
try:
	ccnt = lcnt = 0
	for line in open('text.txt', 'rt'):
		lcnt += 1
		for ch in line:
			print(ch, end='')
			ccnt += 1
	print("\n\nCaracteres en el archivo:", ccnt)
	print("Líneas en el archivo:     ", lcnt)
except IOError as e:
	print("Se produjo un error de E/S: ", strerror(e.errno))
    
    