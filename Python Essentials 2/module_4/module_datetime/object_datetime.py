from datetime import datetime, date, time
dt = datetime(2019,11,4,14,53,00)
print("Fecha y Hora:", dt)
# devuelve el objeto date con el año
print("Fecha:", dt.date())
# devuelve el objeto time con la hora y minuto dados
print("Hora:", dt.time())

# Métodos que devuelven la fecha y hora actual
print("hoy:", datetime.today())
print("ahora:", datetime.now())
print("utc_ahora:", datetime.utcnow())

# Obteniendo una marca de tiempo
dt = datetime(2020, 10, 4, 14, 55)
print("Timestamp:", dt.timestamp())

# Dando formato a la fecha y hora
d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d'))

t = time(14, 53)
print(t.strftime("%H:%M:%S"))

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%y/%B/%d %H:%M:%S"))