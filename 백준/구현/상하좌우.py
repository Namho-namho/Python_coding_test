N = int(input())
plan = input().split()
x, y = 1, 1

# L R U D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ["L", "R", "U", "D"]

for p in plan:
    i = move.index(p)
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
    x = nx
    y = ny
print(x, y)