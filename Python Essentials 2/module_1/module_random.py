from random import random, seed, randrange, randint, choice, sample

# La función random
for i in range(5):
    print(random())
    

# La función seed
seed(0)

for i in range(5):
    print(random())

# Las funciones randrange y randint
print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))
    
for i in range(10):
    print(randint(1, 10), end=',')
    
# Las funciones choice y sample
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))