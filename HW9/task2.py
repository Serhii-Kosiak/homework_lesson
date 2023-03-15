class Employee:
    def __init__(self, name: str, genre: str = None, age: int = None, location: str = None, birth: str = None,
                 specialization: str = None, salary: int = None, working_years: float = 0.0):
        self.name = name
        self.genre = genre
        self.age = age
        self.location = location
        self.birth = birth
        self.specialization = specialization
        self.salary = salary
        self.working_years = working_years

    def increase_salary(self, upsalary):
        self.salary += upsalary

    @staticmethod
    def calculate_bonus(working_years):
        return working_years * 1.15

    @classmethod
    def create_worker_with_name_age(cls, name, age):
        return cls(name=name, age=age)


if __name__ == '__main__':
    maxim = Employee(name='Maxim', genre='Male', age=33, location='California, 33', birth='02.02.1982',
                     specialization='PR', salary=3500, working_years=5)
    maxim.increase_salary(500)
    print(maxim.age)
    print(maxim.salary)
    print(Employee.calculate_bonus(10))
    Vasiliy = Employee.create_worker_with_name_age(name='Vasiliy', age=44)
    Jenia = Employee('Jenia', age=52, salary=4500, location='Berkley', specialization='CEO')
    print(Vasiliy.__dict__)
    print(Jenia.__dict__)
