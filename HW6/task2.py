def square_info(side: [int, float]):
    """
        returns (perimeter, area, diagonal) for square
    """
    # perimeter = 4 * side
    # area = side ** 2
    # diagonal = side * (2 ** 0.5)
    # return perimeter, area, diagonal
    return 4 * side, side ** 2,  side * (2 ** 0.5)


if __name__ == '__main__':
    perimeter, area, diagonal = square_info(10)
    assert perimeter == 40
    assert area == 100
    assert round(diagonal, 2) == 14.14
