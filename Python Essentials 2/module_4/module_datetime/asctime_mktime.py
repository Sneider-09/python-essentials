import time
# objeto struct_time
timestamp = 1572879180
st = time.gmtime(timestamp)
# convierte un objeto struct_time o una tupla en una cadena
print(time.asctime(st))
# convierte un objeto struct_time o una tupla que expresa la hora local al número de segundos desde la época de Unix
print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))