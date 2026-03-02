import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(c):
    q = []
    heapq.heappush(q, (0, c))
    distance[c] = 0
    while q:
        d, now = heapq.heappop(q)
        if distance[now] < d:
            continue
        for j in graph[now]:
            cost = d + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))

dijkstra(c)
city = time = 0
for i in range(1, n+1):
    if distance[i] != INF:
        city += 1
        time =max(distance[i], time) # 총 걸리는 시간
print(city - 1, time) # 시작 노드는 제외