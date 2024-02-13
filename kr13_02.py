def count_numbers(*args):
    return len([num for num in args if num % 4 == 0 and num % 10 == 2])
