from collections import deque

def bfs():
    queue = deque()
    for i in ripe:
        queue.append(i)
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx<0 or ny<0 or nz<0 or nx>=h or ny>=n or nz>=m:
                continue
            if tomato[nx][ny][nz] == -1:
                continue
            elif tomato[nx][ny][nz] == 0:
                tomato[nx][ny][nz] = tomato[x][y][z] + 1
                queue.append((nx, ny, nz))
    # 3차원 리스트에서 최댓값
    max_v = 0
    for i in range(h):
        for j in range(n):
            max_v = max(max_v, max(tomato[i][j]))
    return max_v - 1

m, n, h = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
ripe = []
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                ripe.append((i, j, k))
dx = [0, 0, 0, 0, -1, 1]
dy = [0, 0, -1, 1, 0, 0]
dz = [-1, 1, 0, 0, 0, 0]

date = bfs()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                date = -1
                break
print(date)