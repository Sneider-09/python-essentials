from datetime import timedelta
from datetime import date
from datetime import datetime

delta = timedelta(weeks=2, days=2, hours=3)
print(delta)
print("Días:", delta.days)
print("Segundos:", delta.seconds)
print("Microsegundos:", delta.microseconds)

# Algunas operaciones admitidas por las clases del módulo datetime
delta2 = delta * 2
print(delta2)

d = date(2019, 10, 4) + delta2
print(d)

dt = datetime(2019, 10, 4, 14, 53) + delta2
print(dt)