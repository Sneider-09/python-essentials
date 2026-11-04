def is_year_leap(year):
    #
    # Tu código del LAB anterior.
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
    #

def days_in_month(year, month):
    #
    # Tu código del LAB anterior.
    months = [1,2,3,4,5,6,7,8,9,10,11,12]
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month not in months:
        return None
    elif month == 2 and is_year_leap(year):
        return 29
    else:
        return days[month - 1]
    #

def day_of_year(year, month, day):
    #
    # Escribe tu código nuevo aquí.
    days = 0
    for m in range (1, month):
        md = days_in_month(year, m)
        if md == None:
            return None
        days += md
        
    md = days_in_month(year, month)
    if day >= 1 and day <= md:
        return days + day
    else:
        return None
        
    #

print(day_of_year(2000, 12, 31))
print(day_of_year(2026, 10, 31))
