
class Car:

    # attributes
    # variable inside a class are called attributes
    fuel = None
    brand = None
    model = None

    # custroctor method
    def __init__(self, brand, model, fuel):
        self.brand = brand
        self.model = model
        self.fuel = fuel

    # Methods
    # Function inside a class are called methods
    def start(self):
        print("My car engine started")

    def honk(self):
        print(f"The car with brand:{self.brand} and model:{self.model} Beep Beep!!")

    # Special function used in print()
    def __repr__(self):
        return f"Car with fuel:{self.fuel} and brand:{self.brand} and model:{self.model} "

class EletricCar(Car):

    FUEL = "eletric"
    
    def __init__(self, brand, model):
        super().__init__(brand, model, EletricCar.FUEL)

    def charge(self):
        print(f"The car with model:{self.model} and brand:{self.brand} is charging")

    def start(self):
        super().start()
        print("The batery is decreasing")

class NissanEletric(EletricCar):
    pass

class TeslaEletric(EletricCar):
    
    def connect_to_phone(self):
        print("Tesla is connected to phone")

# henrique_car = {
#     "brand": "Tesla",
#     "model": "X",
#     "fuel": "eletric"
# }

henrique_car = Car("Tesla", "X", "eletric")
# henrique_car.brand = "Tesla"
# henrique_car.model = "X"
# henrique_car.fuel = "eletric"
filomena_car = Car("Porche", "GT", "Diesel")
# filomena_car.brand = "Porche"
# filomena_car.fuel = "Diesel"
# filomena_car.model = "GT"

print("type(henrique) =", type(henrique_car))
print("id(henrique_car) =", id(henrique_car))
print("id(filomena_car) =", id(filomena_car))
print("henrique.brand", henrique_car.brand)
print("filomena.brand", filomena_car.brand)
print("henrique_car =", henrique_car)
print("filomena_car =", filomena_car)

henrique_car.honk()
filomena_car.honk()

rui_car = EletricCar("Nissan", "Leaf")

print("rui_car", rui_car)
print("type(rui_car) =",type(rui_car))

rui_car.charge()
rui_car.honk()
rui_car.start()

