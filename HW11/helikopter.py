from abc import ABC, abstractmethod   # abstract method importing

# encapsulation
# Define the main base class Vehicle


class Vehicle:
    def __init__(self, max_speed):
        self.max_speed = max_speed
    print('Helicopter is created!')

    @abstractmethod
    def recharge(self):  # abstract method creating
        pass

    def in_production(self):  # 1st method in class Vehicle with print function
        print('Started production of Vehicle')

    def accelerate(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def brake(self):
        raise NotImplementedError("Subclass must implement abstract method")


def hover():
    print("Helicopter is hovering...")


def fly():
    print("Helicopter is flying...")


# Define the Helicopter class, which inherits from the Vehicle class
# Inheritance:

class Helicopter(Vehicle):

    def recharge(self):   # implement abstract method
        pass

    def __init__(self, max_speed, rotor_diameter, year, model):
        super().__init__(max_speed)
        self.rotor_diameter = rotor_diameter
        self.year = year      # public attribute
        self.__model = model  # private attribute

    def __get_model(self):  # Private method
        return self.__model

    def get_model(self):  # public method which use private method
        return self.__get_model()

    def get_max_speed(self):
        return self.max_speed

    def set_max_speed(self, new_max_speed):
        self.max_speed = new_max_speed

    def get_rotor_diameter(self):
        return self.rotor_diameter

    def set_rotor_diameter(self, new_rotor_diameter):
        self.rotor_diameter = new_rotor_diameter

    def accelerate(self):
        print("Helicopter is accelerating...")

    def brake(self):
        print("Helicopter is braking...")

    def in_production(self):         # Polymorphism. Using same method for another usage
        print('Start developing and production of Helicopter')


class UFO(Vehicle):
    def brake(self):
        pass

    def accelerate(self):
        pass

    def recharge(self):
        pass

    def __init__(self, max_speed, radius):
        super().__init__(max_speed)
        self._radius = radius
        print('Ufo is created')

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = radius


heli = Helicopter(300, 250, 2023, "Sikorsky")
# heli.in_production()
# car = Vehicle(333)
# car.in_production()
# heli.year = 2005
# hover()
# heli.accelerate()
# fly()
# heli.brake()
# heli.in_production()
ufo = UFO(1500, 300)
ufo.radius = 350  # change radius simply, because we have property and setter
print(ufo.__dict__)
print(heli.__dict__)
