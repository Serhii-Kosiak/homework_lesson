from HW10.Animals import Animals


class Insects(Animals):
    def __init__(self,  name: str, gender: str = None, age: int = None, flying: str = True, groundbase: bool = True,
                 poisoned: bool = True):
        super().__init__(name, gender, age)
        self.__flying = flying
        self.__groundbase = groundbase
        self.__poisoned = poisoned

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
    def groundbase(self):
        return self.__groundbase

    @groundbase.setter
    def groundbase(self, new_groundbase):
        if isinstance(new_groundbase, bool):
            self.__groundbase = new_groundbase
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


    def say_bzz(self):
        print('say hi from Insects to everyone')

if __name__ == '__main__':

    buggie1 = Insects(name='Sarancha', gender='Male', age=1, flying=True, groundbase=True, poisoned=False)
    buggie1.location = 'All continents'
    buggie1.say_bzz()
    print(buggie1.__dict__)
