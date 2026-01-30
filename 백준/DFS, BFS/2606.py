import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n + 1):
    graph[i].sort()

visited = [False]*(n + 1)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    numvisit = 0
    while(queue):
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                numvisit += 1
    return numvisit


print(bfs(graph, 1, visited))