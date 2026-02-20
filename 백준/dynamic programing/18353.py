import sys
input = sys.stdin.readline

n = int(input())
soldier = list(map(int, input().split()))
soldier.reverse()

# d[i] : list[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
# d[i] = max(d[i], d[j] + 1) if list[j] < list[i]

d = [1] * n
for i in range(1, n):
    for j in range(0, i):
        if soldier[j] < soldier[i]:
            d[i] = max(d[i], d[j] + 1)

print(n - max(d))