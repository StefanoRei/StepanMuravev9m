def sort_l():
    lst = []
    n = int(input())
    for i in range(n):
        element = input()
        lst.append(element)
    sort_lst = sorted(lst, key=len)
    return sort_lst
sort= sort_l()
print(sort)
