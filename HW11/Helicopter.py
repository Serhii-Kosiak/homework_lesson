# Define the base class Vehicle
from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, max_speed):
        self.max_speed = max_speed

    @abstractmethod
    def in_production(self):
        pass

    def accelerate(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def brake(self):
        raise NotImplementedError("Subclass must implement abstract method")


# Define the Helicopter class, which inherits from the Vehicle class
def hover():
    print("Helicopter is hovering...")


def fly():
    print("Helicopter is flying...")


class Helicopter(Vehicle, ABC):
    def __init__(self, max_speed, rotor_diameter):
        super().__init__(max_speed)
        self.rotor_diameter = rotor_diameter

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

    def in_production(self):
        print('i am in production in 2023')


# Instantiate a Helicopter object and demonstrate the use of getters, setters, and methods
heli = Helicopter(250, 10)
print(heli.get_max_speed())
heli.set_max_speed(300)
print(heli.get_max_speed())
print(heli.get_rotor_diameter())
hover()
heli.accelerate()
fly()
heli.brake()
heli.in_production()
