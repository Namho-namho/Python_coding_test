import sys

input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
graph = [[INF] * (v+1) for _ in range(v+1)]

for a in range(1, v + 1):
    for b in range(1, v + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(e):
    a, b, c = map(int, input().split())
    if c < graph[a][b]:
        graph[a][b] = c

for k in range(1, v+1):
    for a in range(1, v+1):
        if graph[a][k] ==INF:
            continue
        for b in range(1, v+1):
            if graph[k][b] ==INF:
                continue    
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

cycle = INF

for a in range(1, v+1):
    for b in range(1, v+1):
        if a == b:
            continue
        cycle = min(cycle, graph[a][b] + graph[b][a])
print(-1 if cycle >= INF else cycle)
