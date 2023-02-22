

def squares_for_even(start: int, end: int):
    if start % 2 != 0:
        start += 1

    for num in range(start, end+1, 2):
        if num % 2 == 0:
            yield num ** 2


result = squares_for_even(0, 1000000000)

print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

print(type(result))
