class Car:
    def __init__(self,make,model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f"<Car {self.make} {self.model}>"



class Garage:
    def __init__(self):
        self.cars=[]

    def __len__(self):
        return len(self.cars)

    def add_car(self,car):
        if not isinstance(car,Car):
            raise TypeError(f"Try to add the '{car.__class__.__name__}' to the garage but yu can only add 'Car' objects!! ")
        self.cars.append(car)


renault=Garage()
car=Car('Renault','Duster')
renault.add_car(car)
car2=Car('Reanult','Kwid')
renault.add_car(car2)

print(len(renault))    