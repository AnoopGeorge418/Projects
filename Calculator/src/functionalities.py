def add(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError('Both inputs must be numbers')
        return a + b
    except ValueError as e:
        print(e)

def sub(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError('Both inputs must be numbers')
        return a - b
    except ValueError as e:
        print(e)

def mul(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError('Both inputs must be numbers')
        return a * b
    except ValueError as e:
        print(e)

def div(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError('Both inputs must be numbers')
        if b == 0:
            raise ZeroDivisionError(f'{a} can\'t be divisible by zero.')
        return a / b
    except (ZeroDivisionError, ValueError) as e:
        print(e)

def floor_div(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError('Both inputs must be numbers')
        if b == 0:
            raise ZeroDivisionError(f'{a} can\'t be divisible by zero.')
        return a // b
    except (ZeroDivisionError, ValueError) as e:
        print(e)

def expo(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError('Both inputs must be numbers')
        return a ** b
    except ValueError as e:
        print(e)

def mod(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError('Both inputs must be numbers')
        if b == 0:
            raise ZeroDivisionError(f'{a} can\'t be divisible by zero.')
        return a % b
    except (ZeroDivisionError, ValueError) as e:
        print(e)