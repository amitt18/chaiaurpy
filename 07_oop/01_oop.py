class Car:
    def __init__(self,brand,model):
       self.brand = brand
       self.model = model

    def full_name(self):
        return f"{self.brand}{self.model}"   


my_car = Car("BMW","Corolla")
print(my_car.model)
print(my_car.full_name())
my_new_car = Car("Porshe","x56")
print(my_new_car.brand)
print(my_new_car.model)
print(my_new_car.full_name())