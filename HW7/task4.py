from typing import Sequence


def custom_min(iterable: Sequence):
    minimum = iterable[0]
    for element in iterable:
        if element < minimum:
            minimum = element
    return minimum


def custom_max(iterable: Sequence):
    maximum = iterable[0]
    for element in iterable:
        if element > maximum:
            maximum = element
    return maximum


# Example usage
numbers = [1, 4, 2, 6, 8, 5, 7, 3]
print(custom_min(numbers))
print(custom_max(numbers))

words = ['apple', 'banana', 'cherry', 'date']
print(custom_min(words))
print(custom_max(words))
