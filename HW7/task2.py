def custom_filter(function, iterable):
    result = []
    for element in iterable:
        if function(element):
            result.append(element)
    return result


def is_even(number):
    return number % 2 == 0


def names_from_a(name):
    return name.startswith('A')


names = ['Anna', 'Anastasiya', 'Agata', 'Olga', 'Sveta', 'Yana']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = custom_filter(is_even, numbers)
print(even_numbers)

print(custom_filter(names_from_a, names))
print(custom_filter(lambda x: x.startswith('A'), names))
