from HW10.Mamals import Mammals


class Human(Mammals):

    def __init__(self, name, gender, age, location):
        super().__init__(name, gender, age, location)


if __name__ == '__main__':
    man = Human('gomer', 'Male', 35, 'USA')
    lisa = Human('lisa', 'female', 11, 'USA')
    print(man.__dict__)
    print(lisa.__dict__)
