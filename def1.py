def sum_of_digits(*args):
    for num in args:
        if not isinstance(num, int) or num < 0:
            raise ValueError()
    return [sum(int(digit) for digit in str(num)) for num in args]
