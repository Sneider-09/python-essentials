# Validador IBAN. 
# Datos de prueba
# Inglés: GB72 HBZU 7006 7212 1253 00
# Francés: FR76 30003 03620 00020216907 50
# Alemán: DE02100100100152517108 

# pide al usuario que ingrese el IBAN con espacio
iban = input("Ingresa un IBAN, por favor: ")    
# remueve los espacios en blanco de inmediato        
iban = iban.replace(' ','')                             

# el IBAN ingresado debe constar solo de dígitos y letras
if not iban.isalnum():            
    # muestra un mensaje                      
    print("Has introducido caracteres no válidos.")     
# el IBAN no debe tener menos de 15 caracteres (Noruega)
elif len(iban) < 15:         
    # si es más corto, se informa al usuario                           
    print("El IBAN ingresado es demasiado corto.") 
# además, el IBAN no puede tener más de 31 caracteres (Malta)     
elif len(iban) > 31:       
    # si es más largo, se le informa al usuario                             
    print("El IBAN ingresado es demasiado largo.")   

# se comienza con el procesamiento.   
else:
    # se mueven los cuatro caracteres iniciales al final del número y se convierten todas las letras a mayúsculas
    iban = (iban[4:] + iban[0:4]).upper()   
    # esta es la variable utilizada para completar el número, creada al reemplazar las letras con dígitos            
    iban2 = ''      
    # iterar a través del IBAN                                    
    for ch in iban:      
        # si el carácter es un dígito...                               
        if ch.isdigit():  
            # solo se copia                              
            iban2 += ch     
        # de lo contrario...                            
        else:    
            # ... conviértelo en dos dígitos                                       
            iban2 += str(10 + ord(ch) - ord('A'))      
    # la forma convertida del IBAN está lista: ahora se convierte en un número entero. 
    iban = int(iban2)      
    # ¿el residuo de la división de iban2 entre 97 es igual a 1?                             
    if iban % 97 == 1: 
        # si es así, entonces el número es correcto.                                 
        print("El IBAN ingresado es válido.")   
    # de lo contrario...        
    else:     
        #... el número no es válido.                                          
        print("El IBAN ingresado no es válido.")        
    