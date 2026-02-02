import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(x, y):
    if x < 0 or x > n-1 or y < 0 or y >m-1:
        return False
    if bat[x][y] == 1:
        bat[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

T = int(input())
for _ in range(T):
    count = 0
    m, n, k = map(int, input().split())
    bat = [[0]*m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        bat[b][a] = 1
    for i in range(n):
        for j in range(m):
            if dfs(i,j):
                count += 1
    print(count)