secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

number = int(input("¿Cuál es el número secreto? "))

while secret_number != number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    number = int(input("¿Cuál es el número secreto? "))
    
print( "¡Bien hecho, muggle! Eres libre ahora.")

