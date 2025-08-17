class Car:
    total_car=0
    def __init__(self,brand,model):
       self.__brand = brand
       self.__model = model
       Car.total_car+=1

    def chai_brand(self):
        return self.__brand+"!"
    
    
    def full_name(self):
        return f"{self.__brand}{self.__model}"
    def fuel_type(self):
        return "Petrol ot diesel"
    @staticmethod
    def general_description():
        return "Cars are mean of transport"
    @property
    def model(self):
        return self.__model



class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric battery" 
# my_tesla = ElectricCar("Tesla ", " Model s ", "85kw")
# print(isinstance(my_tesla,Car))
# print(isinstance(my_tesla,ElectricCar))



# my_car = Car("tata","safari")
# my_car.model = "city"
# Car("TATA","nexon")
# print(my_car.general_description())
# print(Car.general_description())
# print(my_car.model)

# safarithree = Car("tata","nexon")
# print(my_car.fuel_type())
# print(Car.total_car)
# my_car = Car("BMW","Corolla")
# print(my_car.model)
# print(my_car.full_name())
# my_new_car = Car("Porshe","x56")
# print(my_new_car.brand)
# print(my_new_car.model)
# print(my_new_car.full_name())



class Battery:
    def batter_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "this is engine"

class ElectricCar2(Battery,Engine,Car):
    pass

my_new_tesla = ElectricCar2("tesla","model s")
print(my_new_tesla.engine_info())
print(my_new_tesla.batter_info())

