import os

# Creando directorios en Python
# os.mkdir("my_first_directory")
print(os.listdir())

# Creación recursiva de directorios
os.makedirs("my_first_directory/my_second_directory")
os.chdir("my_first_directory")
print(os.listdir())

# Sistemas tipo Unix: mkdir -p my_first_directory/my_second_directory
# Windows: mkdir my_first_directory/my_second_directory

# os proporciona una función que devuelve información 
# sobre el directorio de trabajo actual
os.chdir("my_second_directory")
print(os.getcwd())

# Eliminando directorios en Python
os.rmdir("my_first_directory")
os.removedirs("my_first_directory/my_second_directory")
print(os.listdir())

# La función system()
returned_value = os.system("mkdir my_first_directory")
print(returned_value)