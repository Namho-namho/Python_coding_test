from collections import deque

def bfs(x, y):
    que = deque()
    que.append((x, y))
    while(que):
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                que.append((nx, ny))
    return miro[n-1][m-1]

n, m = map(int, input().split())
miro = []
for _ in range(n):
    miro.append(list(map(int, input())))
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
print(bfs(0, 0))