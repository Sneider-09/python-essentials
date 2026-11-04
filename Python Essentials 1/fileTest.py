def f(x):
    if x == 0:
        return 0
    return x + f(x - 1)


print(f(3))

def fun(x):
    x += 1
    return x


x = 2
x = fun(x + 1)
print(x)

dictionary = {}
my_list = ['a', 'b', 'c', 'd']

for i in range(len(my_list) - 1):
    dictionary[my_list[i]] = (my_list[i], )

for i in sorted(dictionary.keys()):
    k = dictionary[i]
    # Inserta tu código aquí.
    print(k)

def func(a, b):
    return a ** a


print(func(2))

def func_1(a):
    return a ** a


def func_2(a):
    return func_1(a) * func_1(a)


print(func_2(2))

try:
    print("Hola")
# A:
except (TypeError, ValueError, ZeroDivisionError):
    # Algo de código.
    print("Hola")

# B:
except TypeError, ValueError, ZeroDivisionError:
    print("Hola")
    # Algo de código.

# C:
except: (TypeError, ValueError, ZeroDivisionError)
    print("Hola")
    # Algo de código.

# D:
except: TypeError, ValueError, ZeroDivisionError
    print("Hola")
    # Algo de código.

# E:
except (TypeError, ValueError, ZeroDivisionError)
    print("Hola")
    # Algo de código.

# F:
except TypeError, ValueError, ZeroDivisionError
    print("Hola")
    # Algo de código.




