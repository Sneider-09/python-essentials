# Probando propiedades: variables de clase.
class Super:
    # supVar = 1
    def __init__(self):
        self.supVar = 11


class Sub(Super):
    # subVar = 2
    def __init__(self):
        super().__init__()
        self.subVar = 12


obj = Sub()

print(obj.subVar)
print(obj.supVar)
    