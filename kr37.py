import string

base = '0123456789abcdefghijklmnopqrstuvwxyz'
def from_base(number):
    a = 0
    res = 0
    for i in number[::-1]:
        res += base.index(i) * (37 ** a)
        a += 1
    return res
x = from_baze(input())
y = from_baze(input())
print(x+y)
