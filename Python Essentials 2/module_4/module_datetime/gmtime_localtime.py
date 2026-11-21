# # time.struct_time:
#     tm_year   # Especifica el año.
#     tm_mon    # Especifica el mes (valor de 1 a 12)
#     tm_mday   # Especifica el día del mes (value from 1 to 31)
#     tm_hour   # Especifica la hora (valor de 0 a 23)
#     tm_min    # Especifica el minuto (valor de 0 a 59)
#     tm_sec    # Especifica el segundo (valor de 0 a 61)
#     tm_wday    # Especifica el día de la semana (valor de 0 a 6)
#     tm_yday   # Especifica el día del año (valor de 1 a 366)
#     tm_isdst  # Especifica si se aplica el horario de verano (1: sí, 0: no, -1: no se sabe)
#     tm_zone   # Especifica el nombre de la zona horaria (valor en forma abreviada)
#     tm_gmtoff # Especifica el desplazamiento al este del UTC (valor en segundos)

import time

timestamp = 1572879180
print(time.gmtime(timestamp))
print(time.localtime(timestamp))