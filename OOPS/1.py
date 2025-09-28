# Question 1:
# Create a Car class with attributes brand, model, and price. 
# Define a method car_info() that prints all details. Then, create two objects with different values and display their info.

class car:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def car_info(self):
        print(f"Car brand : {self.brand}, model:{self.model}, price: {self.price}")

car1 = car("Thar","4x4",1300000)
car2 = car("BMW","M5",130000000)

car1.car_info()
car2.car_info()
print(car2.brand)