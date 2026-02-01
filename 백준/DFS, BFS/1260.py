import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n + 1):
    graph[i].sort()

visitedB = [False]*(n + 1)
visitedD = [False]*(n + 1)

def dfs(graph, v, visitedD):
    visitedD[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visitedD[i]:
            dfs(graph, i, visitedD)

def bfs(graph, v, visitedB):
    queue = deque()
    queue.append(v)
    visitedB[v] = True
    while(queue):
        q = queue.popleft()
        print(q, end=" ")
        for i in graph[q]:
            if not visitedB[i]:
                queue.append(i)
                visitedB[i] = True


dfs(graph, v, visitedD)
print()
bfs(graph, v, visitedB)