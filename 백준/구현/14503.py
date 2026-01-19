N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
total = 0
# 북동남서 0123
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while(True):
    if room[r][c] == 0:
        room[r][c] = "*"
        total += 1
    pro = False
    for _ in range(4):
        d = (d - 1) % 4
        dr = r + dx[d]
        dc = c + dy[d]
        if room[dr][dc] == 0:
            pro = True
            r, c = dr, dc
            break
    if pro == False:
        i = (d + 2) % 4
        dr = r + dx[i]
        dc = c + dy[i]
        if room[dr][dc] == 1:
            break
        r, c = dr, dc
print(total)