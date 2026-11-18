class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Mi nombre es " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        # Nombramos explícitamente la superclase. 
        Super.__init__(self, name)


obj = Sub("Andy")

print(obj)
    
    
class Sub2(Super):
    def __init__(self, name):
        # Hacemos uso de la función super(), la cual accede 
        # a la superclase sin necesidad de conocer su nombre
        super().__init__(name)


obj = Sub2("Andy")

print(obj)
    