from HW10.Mamals import Mammals


class FlyingMammals(Mammals):
    def __init__(self, name: str, gender: str = None, age: int = None, bird: bool = True, warmblood: bool = True):
        super().__init__(name, gender, age)
        self.__bird = bird
        self.__warmblood = warmblood

    @property
    def bird(self):
        return self.__bird

    @bird.setter
    def bird(self, new_bird):
        if isinstance(new_bird, bool):
            self.__bird = new_bird
        else:
            raise ValueError('The bird should be a bool')

    @property
    def warmblood(self):
        return self.__warmblood

    @warmblood.setter
    def warmblood(self, new_warmblood):
        if isinstance(new_warmblood, str):
            self.__warmblood = new_warmblood
        else:
            raise ValueError('The warmblood should be a str')

    def say_hi(self):
        print('say hi from Flying Mammals to everyone')
        print('I am flying over sky')
        print('My passport:')


if __name__ == '__main__':

    eagle = FlyingMammals(name='American Eagle', gender='Male', age=5)
    eagle.location = 'East part of USA'
    eagle.bird = True
    eagle.say_hi()
    print(eagle.__dict__)
