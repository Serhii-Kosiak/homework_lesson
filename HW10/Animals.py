from abc import ABC, abstractmethod


class Animals:
    def __init__(self, name: str, gender: str = None, age: int = None):
        self.__name = name.title()  # private and hide parameter
        self.__gender = gender
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            raise ValueError('The value should be a str')

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, new_gender):
        if new_gender in ["Male", "Female", None]:
            self.__gender = new_gender
        else:
            raise ValueError('Gender should be in ["Male", "Female", None]')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int):
            self.__age = new_age
        else:
            raise ValueError('The value should be a int')

    def say_hi(self):
        print('say hi from Animals to everyone. I will eat you right now')

    def say_bye(self):  # hide function
        print('say goodbye to this world :( ')

    def attack(self):  # using hiding function from one call - lion.attack
        self.say_hi()
        self.say_bye()
        print('Lion get attacked you...')


if __name__ == '__main__':
    lion = Animals('Leopold', 'Male', 3)
    lion.attack()
