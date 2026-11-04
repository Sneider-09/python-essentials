ingreso = float(input("Escriba su ingreso anual: "))

if ingreso < 85528:
    impuesto = ingreso * 0.18 - 556.02
else: 
    impuesto = 14839.02 + (ingreso - 85528) * 0.32

if impuesto < 0:
    impuesto = 0.0

print("El impuesto es:", round(impuesto, 0) ,"pesos")