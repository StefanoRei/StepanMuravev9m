def is_valid_37_base_number(s):
    try:
        int(s, 37)
        return True
    except ValueError:
        return False

num1 = input()
if not is_valid_37_base_number(num1):
    print("err")
    exit()


num2 = input()
if not is_valid_37_base_number(num2):
    print("err")
    exit()

num1_dec = int(num1, 37)
num2_dec = int(num2, 37)
sum_dec = num1_dec + num2_dec

print(sum_dec)
