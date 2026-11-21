from datetime import datetime, date, time

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%F %H:%M:%S"))
print(dt.strftime("%y/%B/%d %H:%M:%S"))
print(dt.strftime("%a, %Y %b %d"))
print(dt.strftime("%A, %Y %B %d"))
print(dt.strftime("Día de la semana: " + "%u"))
print(dt.strftime("Día del año: " + "%j"))
print(dt.strftime("Número de semana en el año: " + "%W"))