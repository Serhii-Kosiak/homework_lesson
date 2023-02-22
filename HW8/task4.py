

def has_three(num: [int, float]):
    return '3' in str(num)


numbers = range(1, 1001)
# numbers_with_three = filter(has_three, numbers)
numbers_with_three = filter(lambda num: '3' in str(num), numbers)

for num in numbers_with_three:
    print(num)
