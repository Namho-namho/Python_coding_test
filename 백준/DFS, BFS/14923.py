from collections import deque

def bfs(x, y):
    queue = deque()
    # chance 1이면 안부숨, 0이면 부숨
    queue.append((x, y, 1))
    # 해당 좌표에서 벽을 부셨는지 여부의 상태로 도달했을때 최단 거리
    dist = [[[-1, -1] for _ in range(m)] for _ in range(n)]
    dist[x][y][1] = 0
    
    while queue:
        x, y, chance = queue.popleft()
        if x == ex-1 and y == ey-1:
            return dist[x][y][chance]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if miro[nx][ny] == 1 and chance == 1 and dist[nx][ny][0] == -1:
                dist[nx][ny][0] = dist[x][y][chance] + 1
                queue.append((nx, ny, 0))
            elif miro[nx][ny] == 0 and dist[nx][ny][chance] == -1:
                dist[nx][ny][chance] = dist[x][y][chance] + 1
                queue.append((nx, ny, chance))
            
    return -1

n, m = map(int, input().split())
hx, hy = map(int, input().split())
ex, ey = map(int, input().split())
miro = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

print(bfs(hx-1, hy-1))