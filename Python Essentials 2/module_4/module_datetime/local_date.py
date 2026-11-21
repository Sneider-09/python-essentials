from datetime import date

today = date.today()

print("Hoy:", today)
print("Año:", today.year)
print("Mes:", today.month)
print("Día:", today.day)

# crear un objeto date
my_date = date(2019, 11, 4)
print(my_date)