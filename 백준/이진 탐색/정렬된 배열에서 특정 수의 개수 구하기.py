from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
array = list(map(int, input().split()))

low = bisect_left(array, x)
high = bisect_right(array, x)
result = high - low

print(result if result > 0 else -1)