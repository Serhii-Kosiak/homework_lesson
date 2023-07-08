from HW11.vehicle import Vehicle


# Define the Helicopter class, which inherits from the Vehicle class
# Inheritance

class Helicopter(Vehicle):

    def __init__(self, max_speed, rotor_diameter, year, model):
        super().__init__(max_speed)
        self.rotor_diameter = rotor_diameter
        self.year = year
        self.model = model

    def recharge(self):
        print("Helicopters don't use recharging, only refueling")

    def fly(self):
        print("Helicopter is flying...")


if __name__ == '__main__':
    heli = Helicopter(300, 250, 2023, "Sikorsky")
    heli.max_speed = 500
    heli.in_production()
    print(heli.__dict__)
