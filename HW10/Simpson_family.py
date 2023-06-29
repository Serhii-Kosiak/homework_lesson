from HW10.Human import Human


class Simpsons(Human):

    def __init__(self, name, gender, age, location):
        super().__init__(name, gender, age, location)


if __name__ == '__main__':

    marge = Simpsons('marge simpson', 'female', 30, 'USA')
    print(marge.__dict__)
