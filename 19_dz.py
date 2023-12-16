n = int(input())
numbers = []

for _ in range(n):
    number = int(input())
    numbers.append(number)

max_binary_digits_number = max(numbers, key=lambda x: len(bin(x))-2)

print(max_binary_digits_number)
