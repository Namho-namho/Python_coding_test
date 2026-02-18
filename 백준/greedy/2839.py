N = int(input())
minbong = -1

for i in range(N // 5, -1, -1):
    n = N - (5 * i)
    if n % 3 == 0:
        minbong = i + n // 3
        break

print(minbong)