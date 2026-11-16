# self -> Permite que el método acceda a entidades 
# (propiedades y actividades / métodos) del objeto

class Stack:
    # Constructor
    def __init__(self):
        # self.stack_list = [] # Público
        self.__stack_list = [] #Privado
    
    # Funciones -> Métodos
    def push(self, val):
        self.__stack_list.append(val)
    
    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val
        
# Hereda de la superclase
class AddingStack(Stack):
    def __init__(self):
        # Invocar explícitamente el constructor de una superclase
        Stack.__init__(self) 
        self.__sum = 0
    
    # Métodos
    def push(self, val):
        self.__sum += val
        Stack.push(self, val)
    
    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val
    
    def get_sum(self):
        return self.__sum
    
        
stack_object = Stack()
# print(len(stack_object.__stack_list))

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())

# Hacer que más de una pila se comporte de la misma manera.
stack_object_1 = Stack()
stack_object_2 = Stack()

stack_object_1.push(3)
stack_object_2.push(stack_object_1.pop())

print(stack_object_2.pop())

# Trabajan independientemente.
little_stack = Stack()
another_stack = Stack()
funny_stack = Stack()

little_stack.push(1)
another_stack.push(little_stack.pop() + 1)
funny_stack.push(another_stack.pop() - 2)

print(funny_stack.pop())


# Comprobar subclase y superclase
stack_object = AddingStack()

for i in range(5):
    stack_object.push(i)
print(stack_object.get_sum())

for i in range(5):
    print(stack_object.pop())