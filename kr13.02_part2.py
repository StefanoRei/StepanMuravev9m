def remove_values():
    lst = list(map(int, input().split()))
    val = int(input())
    return [x for x in lst if x != val]
print(remove_values())
