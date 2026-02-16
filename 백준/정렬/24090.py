import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def quick_sort(array, low, high):
    if low < high:
        pivotpoint = partition(array, low, high)
        quick_sort(array, low, pivotpoint - 1)
        quick_sort(array, pivotpoint + 1, high)

def do_swap(array, i, j):
    global cmt, k
    array[i], array[j] = array[j], array[i]
    cmt += 1
    if cmt == k:
        a, b = array[i], array[j]
        if a <= b:
            print(a, b)
        else:
            print(b, a)
        sys.exit(0)

def partition(array, low, high):
    pivotitem = array[high]     
    i = low - 1
    for j in range(low, high):  
        if array[j] <= pivotitem:
            i += 1
            do_swap(array, i, j)
    if i + 1 != high:           
        do_swap(array, i + 1, high)
    return i + 1

n, k = map(int, input().split())
array = list(map(int, input().split()))
cmt = 0

quick_sort(array, 0, n - 1)
print(-1)
