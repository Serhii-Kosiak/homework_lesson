

def my_all(sequence) -> bool:
    if len(sequence) == 0:
        return True
    else:
        for element in sequence:
            if bool(element) is False:
                return False
        return True


if __name__ == '__main__':
    assert my_all([])
    assert my_all([1, 2, 3])
    assert my_all([0, 2, 3]) is False
