def binary_search(a, x, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if a[mid] == x:
        return 1
    elif a[mid] > x:
        return binary_search(a, x, start, mid - 1)
    else:
        return binary_search(a, x, mid + 1, end)


n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
b = list(map(int, input().split()))

for i in b:
    print(binary_search(a, i, 0, n - 1))