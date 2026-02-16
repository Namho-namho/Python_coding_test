from collections import deque

def bfs(nx, ny, gx, gy):
    if nx == gx and ny == gy:
        return 0
    queue = deque()
    queue.append((nx, ny))
    chessSheet[nx][ny] = 0
    while(queue):
        nx, ny = queue.popleft()
        for i in range(8):
            x = nx + dx[i]
            y = ny + dy[i]
            if x < 0 or y < 0 or x > l - 1 or y > l - 1:
                continue
            if chessSheet[x][y] == -1:
                chessSheet[x][y] = chessSheet[nx][ny] + 1
                if x == gx and y == gy:
                    return chessSheet[x][y]
                queue.append((x, y))

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2, -2, -1, 1, 2]

n = int(input())
for _ in range(n):
    l = int(input())
    nx, ny = map(int, input().split())
    gx, gy = map(int, input().split())
    chessSheet = [[-1] * (l) for _ in range(l)]
    print(bfs(nx, ny, gx, gy))