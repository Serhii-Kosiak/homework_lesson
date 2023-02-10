def square_info(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = side * (2 ** 0.5)
    return perimeter, area, diagonal

side = 10
perimeter, area, diagonal = square_info(side)

print(f'perimeter is {perimeter}, area is {area}, diagonal is {diagonal}')



# if __name__ == '__main__':
# pass