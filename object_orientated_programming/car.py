# This program defines a class for a Car and simulates driving the car.

class Car:
    def __init__(self, make, model, year, mileage, fuel):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel = fuel

    def drive(self, miles):
        if self.fuel <= 0:
            print("The car is out of fuel.")
        else:
            self.mileage += miles
            self.fuel -= miles / 20
            print("Drove", miles, "miles. Mileage:", self.mileage, "Fuel:", self.fuel)

    def fill_up(self):
        self.fuel = 15
        print("Filled up tank. Fuel:", self.fuel)

# Create an instance of the Car class
car = Car("Honda", "Civic", 2015, 50000, 10)

# Drive the car and fill up the tank
car.drive(100)
car.drive(50)
car.fill_up()
car.drive(200)

# Print the car's make, model, year, mileage, and current fuel level
print("Make:", car.make)
print("Model:", car.model)
print("Year:", car.year)
print("Mileage:", car.mileage)
print("Fuel:", car.fuel)
