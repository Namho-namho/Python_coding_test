k, n = map(int, input().split())
h = []
for _ in range(k):
    h.append(int(input()))

start = 1 # 길이는 무조건 1
end = max(h)
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in h:
        # if i > mid 조건은 필요없음 -> i == mid : 1, i < mid : 0
        total += (i//mid)
    if total < n:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)