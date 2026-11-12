# El método isspace() identifica espacios en blanco 
# solamente, no tiene en cuenta ningún otro carácter 
# (el resultado es entonces False).
print(' \n '.isspace()) #-> True
print(" ".isspace()) #-> True
print("mooo mooo mooo".isspace()) #-> False