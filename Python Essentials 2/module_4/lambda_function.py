# función anónima sin parámetros que siempre devuelve un 2
two = lambda: 2
# función anónima de un parámetro que devuelve el valor de su argumento al cuadrado
sqr = lambda x: x * x
# toma dos parámetros y devuelve el valor del primero elevado al segundo
pwr = lambda x, y: x ** y

for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))

# Queremos que print_function sea universal, debería 
# aceptar un conjunto de argumentos incluidos en una 
# lista y una función a ser evaluada, ambos como 
# argumentos; no queremos codificar nada.
def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')

def poly(x):
    return 2 * x**2 - 4 * x + 2

print_function([x for x in range(-2, 3)], poly)

# beneficio que puede aportar una función lambda.
print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)
    