from datetime import datetime
import time
# crea un objeto datetime a partir de una cadena que representa una fecha y una hora
print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))
# analiza una cadena que representa un tiempo en un objeto struct_time.
print(time.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))