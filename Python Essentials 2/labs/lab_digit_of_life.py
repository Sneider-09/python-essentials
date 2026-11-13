birthday = input("Ingrese su fecha de cumpleaños (AñoMesDia)")
digit = 0
# Quitar todos los espacios.
birthday = birthday.replace(' ','')

if birthday.isdigit():
    while len(birthday) > 1:
        digit = 0
        
        for d in birthday:
            digit += int(d)
        
        birthday = str(digit)
             
else:
    print("Fecha inválida")

print(birthday)