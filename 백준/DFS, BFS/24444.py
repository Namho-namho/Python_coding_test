from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n + 1):
    graph[i].sort()

visited = [False] * (n + 1)

# 전역 변수 안쓰고 return으로 빼내는 logic
def bfs(visited, r, graph):
    queue = deque([r])
    visited[r] = True
    seq = [0] * (n + 1)
    s = 1
    seq[r] = s
    while(queue):
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                s += 1
                seq[i] = s
    return seq

seq = bfs(visited, r, graph)
for i in range(1, n+1):
    print(seq[i])