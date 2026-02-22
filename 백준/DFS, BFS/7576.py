from collections import deque

def bfs():
    queue = deque()
    for i in ripe:
        queue.append(i)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if tomato[nx][ny] == -1:
                continue
            elif tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                queue.append((nx, ny))
    return max(map(max, tomato)) - 1 # 각 행마다 max 적용


m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
ripe = []
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            ripe.append((i, j))
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

date = bfs()
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            date = -1
            break
print(date)