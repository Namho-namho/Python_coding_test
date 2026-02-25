n = int(input())
color = [list(map(int, input().split())) for _ in range(n)]

# d[i][0] : i번째에서 0으로 칠햇을때 최소값
d = [[0]*3 for _ in range(n)]
d[0] = color[0]

for i in range(1, n):
    d[i][0] = color[i][0] + min(d[i-1][1], d[i-1][2])
    d[i][1] = color[i][1] + min(d[i-1][0], d[i-1][2])
    d[i][2] = color[i][2] + min(d[i-1][0], d[i-1][1])

print(min(d[n-1]))