def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def main():
    n = int(input())
    if n <= 0:
        print()
        return

    arr = []
    for i in range(n):
        num = int(input(f{i+1}:))
        if num <= 0:
            print()
            return
        arr.append(num)

    bubble_sort(arr)

    print(arr)

if __name__ == "__main__":
    main()
