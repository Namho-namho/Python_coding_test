import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance = [INF] * (v + 1)
    distance[start] = 0
    while(q):
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for j in graph[now]:
            cost = dist + j[1]
            if distance[j[0]] > cost:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))
    return distance

d1 = dijkstra(1)
d2 = dijkstra(v1)
d3 = dijkstra(v2)

sum1 = d1[v1] + d2[v2] + d3[v]
sum2 = d1[v2] + d2[v] + d3[v1]

sum = min(sum1, sum2)

print(-1 if sum >= INF else sum)