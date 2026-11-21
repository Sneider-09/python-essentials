import calendar

# La función setfirstweekday()
calendar.setfirstweekday(calendar.SUNDAY)
calendar.prmonth(2026, 12)

# La función weekday()
# verificar el día de la semana en que cae el 24 de diciembre de 2026
print(calendar.weekday(2026, 12, 24))

# La función weekheader()
# obtener nombres cortos de días de la semana
print(calendar.weekheader(2))