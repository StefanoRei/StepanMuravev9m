def check_number(n):
    even = [0, 2, 4, 6, 8]
    odd = [1, 3, 5, 7, 9]
    n = str(n)
    for i in range(4):
        if (int(n[i]) in even and int(n[i+1]) in even) or (int(n[i]) in odd and int(n[i+1]) in odd):
            return False
    return True

count = 0
n = int(input("))
for count in range(n):
    number = int(input())
    if check_number(number):
        count += 1

print(count)
