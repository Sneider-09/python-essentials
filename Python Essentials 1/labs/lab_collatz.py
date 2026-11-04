c0 = int(input("Ingrese un numero: "))
attemps = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 /= 2
    else: 
        c0 = 3 * c0 + 1
        
    print(int(c0))
    
    attemps += 1

print("pasos =", attemps)