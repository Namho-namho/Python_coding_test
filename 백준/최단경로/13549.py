# bfs
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
        # 0-1 BFS
        if 0 <= 2*v <= MAX and visited[2*v] == -1:
            queue.appendleft(2*v)
            visited[2*v] = visited[v]
        for i in (v - 1, v + 1):
            if 0<=i<=MAX and visited[i] == -1:
                queue.append(i)
                visited[i] = visited[v] + 1
        
n, m = map(int, input().split())
MAX = 100000
visited = [-1] * (MAX + 1)
print(bfs(n, m))

#dijkstra
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
MAX = 100000

n, k = map(int, input().split())
distance = [INF] * (MAX + 1)

def dijkstra(n, k):
    q = []
    heapq.heappush(q, (0, n))
    distance[n] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        if now == k:
            return dist
        for j in (2*now, now-1, now+1):
            if 0 <= j <= MAX:
                if j == 2*now:
                    cost = dist
                else:
                    cost = dist + 1
                if cost < distance[j]:
                    distance[j] = cost
                    heapq.heappush(q, (cost, j))

print(dijkstra(n, k))