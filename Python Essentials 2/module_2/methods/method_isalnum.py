# El método sin parámetros llamado isalnum() comprueba 
# si la cadena contiene solo dígitos o caracteres 
# alfabéticos (letras) y devuelve True (verdadero) 
# o False (falso) de acuerdo al resultado.

# Demostración del método isalnum():
print('lambda30'.isalnum()) #-> True
print('lambda'.isalnum()) #-> True
print('30'.isalnum()) #-> True
print('@'.isalnum()) #-> False
print('lambda_30'.isalnum()) #-> False
print(''.isalnum()) #-> False

t = 'Six lambdas'
print(t.isalnum()) #-> False

t = '&Alpha;&beta;&Gamma;&delta;'
print(t.isalnum()) #-> False

t = '20E1'
print(t.isalnum()) #-> True
