class Vehicle:
    pass
 
 
class LandVehicle(Vehicle):
    pass
 
 
class TrackedVehicle(LandVehicle):
    pass

for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        # issubclass() puede verificar si una clase particular es una subclase de cualquier otra clase.
        print(cls1.__name__ , 'es una subclase de:', cls2.__name__, issubclass(cls1, cls2), end="\t")
    print()
    
my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
my_tracked_vehicle = TrackedVehicle()

for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        # isinstance() devuelve True si el objeto es una instancia de la clase, o False de lo contrario.
        print(isinstance(obj, cls), end="\t")
    print()