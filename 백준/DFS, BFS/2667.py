import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(x, y):
    global count
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        count += 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip())))

count = 0
countG = []
for i in range(n):
    for j in range(n):
        if dfs(i, j):
            countG.append(count)
            count = 0

countG.sort()
print(len(countG))
for c in countG:
    print(c)