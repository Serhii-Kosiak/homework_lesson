from HW10.Mamals import Mammals


class EarthMammals(Mammals):
    def __init__(self, name: str, gender: str = None, age: int = None, cats: bool = True, dogs: True = str):
        super().__init__(name, gender, age)
        self.__cats = cats
        self.__dogs = dogs

    @property
    def cats(self):
        return self.__cats

    @cats.setter
    def cats(self, new_cat):
        if isinstance(new_cat, bool):
            self.__cats = new_cat
        else:
            raise ValueError('The cats should be a bool')

    @property
    def dogs(self):
        return self.__dogs

    @dogs.setter
    def dogs(self, new_dogs):
        if isinstance(new_dogs, str):
            self.__dogs = new_dogs
        else:
            raise ValueError('The dogs should be a str')

    def say_meow(self):
        print('say meow to everyone')
        print('I am cat')


if __name__ == '__main__':
    dog_1 = EarthMammals(name='Sharik', gender='Male', age=3)
    dog_1.location = 'East part of Canada'
    dog_1.cats = False
    dog_1.say_hi()
    print(dog_1.__dict__)
