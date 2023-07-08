from HW11.vehicle import Vehicle


class UFO(Vehicle):

    def __init__(self, max_speed: int, radius: int, stolen_people: int = 0):
        self._radius = radius
        self.__stolen_people = stolen_people
        super().__init__(max_speed)

    # encapsulation:
    @property
    def stolen_people(self):
        if self.__stolen_people > 10:
            print(f'{self.__stolen_people}: You stole enough, please stop, try tomorrow')
        else:
            print(f'{self.__stolen_people}: Maybe stole more today?')
        return self.__stolen_people

    @stolen_people.setter
    def stolen_people(self, value):
        if isinstance(value, int):
            self.__stolen_people = value
        else:
            raise ValueError('The value should be integer')

    def stole_people(self, value):
        if isinstance(value, int):
            self.__stolen_people = self.__stolen_people + value
        else:
            raise ValueError('The value should be integer')

    # polymorphism:
    def fly(self):
        print("UFO is flying...")

    @property
    def radius(self) -> int:
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = radius


if __name__ == '__main__':
    ufo = UFO(1500, 300)
    # ufo.radius = 350  # change radius simply, because we have property and setter
    print(ufo.stolen_people)

    ufo.stolen_people = 1
    print(ufo.stolen_people)
    print(ufo.__dict__)

    ufo.stole_people(5)
    print(ufo.stolen_people)

    ufo.stole_people(5)
    print(ufo.stolen_people)

    ufo.fly()

