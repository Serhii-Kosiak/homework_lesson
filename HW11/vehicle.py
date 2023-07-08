from abc import ABC, abstractmethod  # abstract method importing
# encapsulation
# Define the main base class Vehicle


class Vehicle(ABC):
    def __init__(self, max_speed):
        self.max_speed = max_speed
        print('Vehicle init is called!')

    @abstractmethod
    def recharge(self):
        pass

    @staticmethod
    def in_production():
        print('Started production')

    @staticmethod
    def fly():
        print("Is flying...")
