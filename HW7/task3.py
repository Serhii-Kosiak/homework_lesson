from typing import Callable, Sequence


def custom_map(func: Callable, seq: Sequence):
    result = []
    for element in seq:
        result.append(func(element))
    return result


# custom_map for int
int_seq = [1, 2, 3, 4, 5]
int_result = custom_map(lambda x: x**2, int_seq)
print(int_result)

# custom_map for float
float_seq = [0.1, 0.2, 0.3, 0.4, 0.5]
float_result = custom_map(lambda x: x*2, float_seq)
print(float_result)

# custom_map for list of strings
string_seq = ['apple', 'banana', 'cherry']
string_result = custom_map(lambda x: x.title(), string_seq)
print(string_result)
