def arithmetic(left_operand, right_operand, operation):
    """
        Apply arithmetic operation for provided left and right operands
    """
    # action_dict = {
    #     '+': left_operand + right_operand,
    #     '-': left_operand - right_operand,
    #     '*': left_operand * right_operand,
    #     '/': left_operand / right_operand,
    # }
    #
    # if operation not in action_dict:
    #     return f'Not known operation: {operation}'
    #
    # return action_dict[operation]

    if operation == '+':
        return left_operand + right_operand
    elif operation == '-':
        return left_operand - right_operand
    elif operation == '*':
        return left_operand * right_operand
    elif operation == '/':
        return left_operand / right_operand
    else:
        return f'Not known operation: {operation}'


if __name__ == "__main__":
    assert arithmetic(3, 4, operation="*") == 12
    assert arithmetic(3, 4, operation="+") == 7
    assert arithmetic(25, 5, operation="/") == 5
    assert type(arithmetic(25, 5, operation="/")) == float
    assert arithmetic(5, 5, operation="//") == f"Not known operation: //"
    assert arithmetic.__doc__ == (
        f"\n{' ' * 8}"
        f"Apply arithmetic operation for provided left and right operands\n"
        f"{' ' * 4}"""
    )
    assert arithmetic.__code__.co_name == "arithmetic"
    assert arithmetic.__code__.co_varnames == ("left_operand", "right_operand", "operation")
    try:
        arithmetic(1, 2, 3)
    except TypeError as e:
        assert e.__class__ is TypeError
    try:
        arithmetic(left_operand=1, right_operand=2, operation="+")
    except TypeError as e:
        assert e.__class__ is TypeError

    try:
        arithmetic(1, right_operand=2, operation="+")
    except TypeError as e:
        assert e.__class__ is TypeError
