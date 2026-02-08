from bisect import bisect_left, bisect_right

def search(array, x):
    return bisect_right(array, x) - bisect_left(array, x)

n = int(input())
array = list(map(int, input().split()))
array.sort()
m = int(input())
sangun = list(map(int, input().split()))

for i in sangun:
    print(search(array, i), end=" ")