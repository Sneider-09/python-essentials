import calendar  

c = calendar.Calendar(calendar.SUNDAY)

for weekday in c.iterweekdays():
    print(weekday, end=" ")

# El método itermonthdates()
c = calendar.Calendar()
# Devuelve todos los días del mes y año especificados
for date in c.itermonthdates(2019, 11):
    print(date, end=" ")

# El método itermonthdays()
c = calendar.Calendar()
# Devuelve los días de la semana representados por números
for iter in c.itermonthdays(2019, 11):
    print(iter, end=" ")

# El método monthdays2calendar()
c = calendar.Calendar()
# devuelve una lista de semanas en un mes específico
for data in c.monthdays2calendar(2020, 12):
    print(data)