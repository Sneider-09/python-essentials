def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
 
# Los generadores también se pueden usar con listas por comprensión,
t = [x for x in powers_of_2(5)]
print(t)

# La función list() puede transformar una serie de invocaciones de generador subsequentes en una lista
t2 = list(powers_of_2(3))
print(t2)

# El contexto creado por el operador in también te permite usar un generador
for i in range(20):
    if i in powers_of_2(4):
        print(i)
        
# El generador de números Fibonacci
def fibonacci(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n
 
fibs = list(fibonacci(10))
print(fibs)

# Expresión condicional
the_list = []

for x in range(10):
    the_list.append(1 if x % 2 == 0 else 0)

print(the_list)

the_list_2 = [1 if x % 2 == 0 else 0 for x in range(10)]
print(the_list_2)

# Los corchetes hacen una comprensión, los paréntesis hacen un generador.
the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
len(the_list)
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))
len(the_generator)
 
for v in the_list:
    print(v, end=" ")
print()
 
for v in the_generator:
    print(v, end=" ")
print()