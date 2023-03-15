class Company:
    def __init__(self, name: str, founded: str, ceo: str, location: str, employees: int, capital: int = None,
                 nasdaq: str = None):
        self.__name = name.capitalize()
        self.founded = founded
        self.ceo = ceo
        self.location = location
        self.employees = employees
        self.__capital = capital
        self.nasdaq = nasdaq

    # def set_name(self, new_name: str):
    #     if isinstance(new_name, str):
    #         self.__name = new_name.capitalize()
    #     else:
    #         print('Not allowed to change name')

    @property
    def capital(self):
        return self.__capital

    @capital.setter
    def capital(self, value):
        self.__capital = value

    def include_company(self, company):
        self.employees += company.employees
        self.capital += company.capital


if __name__ == '__main__':

    apple = Company('Apple Company', '01.04.1976', 'Tim Cook', 'California, USA', 2, 200, 'AAPL')
    toshiba = Company('toshiba Company', '1875', 'Tanaka Hisasige', 'Tokyo, Japan', 5, 500, '6502')

    print(apple.__dict__)
    print(toshiba.__dict__)

    apple.include_company(toshiba)
    print(apple.__dict__)






