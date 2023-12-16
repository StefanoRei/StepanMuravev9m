n = int(input("Введите количество чисел: "))
numbers = []

for _ in range(n):
    number = int(input("Введите число: "))
    numbers.append(number)

# Находим число с максимальным количеством разрядов в двоичном представлении
max_binary_digits_number = max(numbers, key=lambda x: len(bin(x))-2)

print("Число с максимальным количеством разрядов в двоичном представлении: ", max_binary_digits_number)
