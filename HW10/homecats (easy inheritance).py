from HW10.Cats import Cats


class homecats(Cats):
    birthday = None  # third new parameter for new class who inheritance main class Cats using "type" and "colour"

    def __init__(self, type, colour, birthday='28.06.2023'):  # default value for birthday changed to 28.06.2023
        super(homecats, self).__init__(type, colour)
        self.birthday = birthday


Murka = homecats('cat', 'Black')
print(Murka.__dict__)
