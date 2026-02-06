from collections import deque
import sys
input = sys.stdin.readline

def bfs(n, m):
    queue = deque([n])
    visited[n] = 0
    while(queue):
        v = queue.popleft()
        if v == m:
            return visited[v]
        for i in (v - 1, v + 1, 2 * v):
            if 0<=i<=MAX and visited[i] == -1:
                queue.append(i)
                visited[i] = visited[v] + 1
        

n, m = map(int, input().split())
MAX = 100000
visited = [-1] * (MAX + 1)
print(bfs(n, m))