from HW10.Animals import Animals


class Mammals(Animals):
    def __init__(self,  name: str, gender: str = None, age: int = None, location: int = None):
        super().__init__(name, gender, age)
        self.__location = location

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, new_location):
        if isinstance(new_location, str):
            self.__location = new_location
        else:
            raise ValueError('The value should be a str')

    def say_hi(self):
        print('say hi from Mammals to everyone')
