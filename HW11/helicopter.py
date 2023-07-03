from HW11.vehicle import Vehicle


# Define the Helicopter class, which inherits from the Vehicle class
# Inheritance

class Helicopter(Vehicle):

    def recharge(self):
        pass

    def __init__(self, max_speed, rotor_diameter, year, model):
        super().__init__(max_speed)
        self.rotor_diameter = rotor_diameter
        self.year = year  # public attribute
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

    def fly(self):
        print("Helicopter is flying...")


heli = Helicopter(300, 250, 2023, "Sikorsky")
heli.in_production()
heli.set_rotor_diameter(500)
print(heli.__dict__)
