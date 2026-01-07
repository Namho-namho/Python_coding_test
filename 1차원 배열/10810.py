import sys
input = sys.stdin.readline

N, M = map(int, input().split())

#bag = [0 for _ in range(N)]
bag = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    for a in range(i, j + 1):
        bag[a - 1] = k
print(*bag)