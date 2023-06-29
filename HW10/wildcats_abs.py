from abc import ABC, abstractmethod   # abstract method importing


class Game(ABC):
    def __init__(self, manufacturer: str, release: int, multiplayer: str = None):
        self.manufacturer = manufacturer
        self.release = release
        self.multiplayer = multiplayer

    @abstractmethod
    def do_work(self):  # abstract method creating
        pass


class Strategy(Game):

    def __init__(self, manufacturer, release, multiplayer, price: float):
        super().__init__(manufacturer, release, multiplayer)
        self.price = price

    def do_work(self):   # abstract method using
        print('I am multiplayer game for sales')


if __name__ == '__main__':
    diablo = Strategy("Blizzard", 2002, 'Yes', 20.0)
    diablo.do_work()
