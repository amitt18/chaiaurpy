class Car:
    def __init__(self,brand,model):
       self.__brand = brand
       self.model = model

    def chai_brand(self):
        return self.__brand+"!"
    
    
    def full_name(self):
        return f"{self.__brand}{self.model}"
    def fuel_type(self):
        return "Petrol ot diesel"   

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric battery" 
my_tesla = ElectricCar("Tesla ", " Model s ", "85kw")
# print(my_tesla.__brand)
print(my_tesla.fuel_type())

safari = Car("tata","safari")
print(safari.fuel_type())
# my_car = Car("BMW","Corolla")
# print(my_car.model)
# print(my_car.full_name())
# my_new_car = Car("Porshe","x56")
# print(my_new_car.brand)
# print(my_new_car.model)
# print(my_new_car.full_name())