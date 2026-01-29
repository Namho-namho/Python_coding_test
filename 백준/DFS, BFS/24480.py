import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n+1):
    graph[i].sort(reverse=True)

visited = [False] * (n + 1)
seq = [0] * (n + 1)
s = 0

def dfs(graph, r, visited):
    global s
    visited[r] = True
    s += 1
    seq[r] = s
    for i in graph[r]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, r, visited)
for i in range(1, n+1):
    print(seq[i])