def get_divisors(num):
    divisors = []
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors.append(i)
            if i != num // i:
                divisors.append(num // i)
    divisors.sort(reverse=True)
    return divisors
def find_numbers_with_4_divisors(a, b):
    numbers_with_4_divisors = []
    for num in range(a, b + 1):
        divisors = get_divisors(num)
        if len(divisors) == 4:
            numbers_with_4_divisors.append(num)
    return numbers_with_4_divisors
a = int(input())
b = int(input())
result = find_numbers_with_4_divisors(a, b)
print(result)
