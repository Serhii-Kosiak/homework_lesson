class Cats:
    type = None
    colour = None  # Basic main class parameter

    def __init__(self, type, colour):
        self.type = type
        self.colour = colour
        self.get_info()

    def get_info(self):
        print("Type: ", self.type, " Colour: ", self.colour, sep='')

