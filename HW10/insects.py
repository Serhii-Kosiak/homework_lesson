from HW10.Animals import Animals


class Insects(Animals):
    def __init__(self, name: str, gender: str = None, age: int = None, flying: bool = True, ground: bool = True,
                 poisoned: bool = True):
        super().__init__(name, gender, age)
        self.__flying = flying
        self.__poisoned = poisoned
        self.__ground = ground


class Butterfly(Insects):
    def __init__(self, name, gender, age, location: str = 'USA'):
        super().__init__(name, gender, age)
        self.__location = location

    @property
    def flying(self):
        return self.__flying

    @flying.setter
    def flying(self, new_flying):
        if isinstance(new_flying, str):
            self.__flying = new_flying
        else:
            raise ValueError('The value should be a str')

    @property
    def ground(self):
        return self.__ground

    @ground.setter
    def ground(self, new_ground):
        if isinstance(new_ground, bool):
            self.__ground = new_ground
        else:
            raise ValueError('The value should be a bool')

    @property
    def poisoned(self):
        return self.__poisoned

    @poisoned.setter
    def poisoned(self, new_poisoned):
        if isinstance(new_poisoned, str):
            self.__poisoned = new_poisoned
        else:
            raise ValueError('The value should be a bool')


if __name__ == '__main__':
    buggie1 = Insects(name='Sarancha', gender='Male', age=1, flying=True, ground=True, poisoned=False)
    buggie1.location = 'All continents'
    print(buggie1.__dict__)
    babochka = Butterfly(name="Babochka", gender="Male", age=2)
    print(babochka.__dict__)
