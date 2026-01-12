N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]
coin.reverse()
result = 0

for c in coin:
    if K >= c:
        result += K // c
        K %= c
    else:
        continue

print(result)