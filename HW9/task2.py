class Employee:
    def __init__(self, name: str, gender: str = None, age: int = None, location: str = None, birth: str = None,
                 salary: int = None, working_years: float = 0.0):
        self.__name = name.capitalize()
        self.__gender = self.set_gender(gender)
        self.__age = age
        self.__location = location
        self.__birth = birth
        self.__salary = salary
        self.__working_years = working_years

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) <= 20:
            self.__name = new_name
        else:
            raise ValueError('The name should be a str with len <= 20')

    @property
    def gender(self):
        return self.__gender

    @staticmethod
    def set_gender(gender):
        if gender in ['Male', 'Female', None]:
            return gender
        else:
            raise TypeError('The are only 2 genders on the Earth for people')

    @gender.setter
    def gender(self, gender_value):
        self.set_gender(gender_value)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int) and new_age <= 70:
            self.__age = new_age
        else:
            raise ValueError('Age should be <= 70. Take your bonus and go to vacation :)')

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, new_location):
        if isinstance(new_location, str) and len(new_location) <= 50:
            self.__location = new_location
        else:
            raise ValueError('The location should be a str with len <= 50')

    @property
    def birth(self):
        return self.__birth

    @property
    def salary(self):
        return self.__salary

    @staticmethod
    def calculate_bonus(working_years):
        return working_years * 1.25

    @classmethod
    def create_worker_with_name_age(cls, name, age):
        return cls(name=name, age=age)


if __name__ == '__main__':
    maxim = Employee(name='Maxim', gender='Male', age=75, location='California, 33', birth='02.02.1982',
                     salary=3500, working_years=5)

    print(maxim.calculate_bonus(10))

    Vasiliy = Employee.create_worker_with_name_age(name='Vasiliy', age=44)
    Jenia = Employee.create_worker_with_name_age('Jenia', 20)

    maxim.gender = 'Female'

    print(maxim.__dict__)
    print(Jenia.__dict__)
    print(Vasiliy.__dict__)
