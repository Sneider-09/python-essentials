# El método endswith() comprueba si la cadena dada termina 
# con el argumento especificado y devuelve True(verdadero) 
# o False(falso), dependiendo del resultado.

# Demostración del método endswith():
if "epsilon".endswith("on"):
    print("si")
else:
    print("no")
    
t = "zeta"
print(t.endswith("a")) #-> True
print(t.endswith("A")) #-> False
print(t.endswith("et")) #-> False
print(t.endswith("eta")) #-> True