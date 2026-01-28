# 재귀 한도 올리기
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m, r = map(int, input().split())
V = [i for i in range(1, n + 1)]
# graph 만들기
E = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    E[a].append(b)
    E[b].append(a)
for i in range(1, n+1):
    E[i].sort()

visited = [False] * (n+1)
seq = [0] * (n+1)
s = 0

def dfs(visited, E, R):
    global s
    visited[R] = True
    s += 1
    seq[R] = s
    for i in E[R]:
        if visited[i] == False:
            dfs(visited, E, i)

dfs(visited, E, r)
for i in range(1, n+1):
    print(seq[i])