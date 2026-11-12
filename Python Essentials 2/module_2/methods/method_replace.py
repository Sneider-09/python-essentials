# El método replace() con dos parámetros devuelve una 
# copia de la cadena original en la que todas las 
# apariciones del primer argumento han sido reemplazadas 
# por el segundo argumento.
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org")) #-> www.pythoninstitute.org
print("This is it!".replace("is", "are")) #-> Thare are it!
print("Apple juice".replace("juice", "")) #-> Apple

# La variante del método replace() con tres parámetros 
# mplea un tercer argumento (un número) para limitar 
# el número de reemplazos.
print("This is it!".replace("is", "are", 1)) #-> Thare is it!
print("This is it!".replace("is", "are", 2)) #-> Thare are it!