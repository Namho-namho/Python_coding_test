n, m = map(int, input().split())
worth = [int(input()) for _ in range(n)]

# ai-k 가능 : ai = min(ai, ai-k + 1)
# ai-k 불가능 : ai = INF

d = [10001]*(m+1)
d[0] = 0
for i in worth:
    for j in range(i, m + 1):
        d[j] = min(d[j], d[j - i] + 1)

print(-1 if d[m] == 10001 else d[m])