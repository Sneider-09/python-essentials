# Pregunta 1: ¿Cuál es el resultado del siguiente fragmento de código? -> False
x = 1
y = 0
 
z = ((x == y) and (x == y)) or not(x == y)
print(not(z))

# Pregunta 2: ¿Cuál es el resultado del siguiente fragmento de código? -> 0 5 -5 1 1 160 5 -5 1 1 16
x = 4
y = 1
 
a = x & y
b = x | y
c = ~x  # ¡difícil!
d = x ^ 5
e = x >> 2
f = x << 2
 
print(a, b, c, d, e, f)

# 
 