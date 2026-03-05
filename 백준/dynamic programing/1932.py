n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

d = []
for i in range(1, n + 1):
    d.append([0] * i)
d[0] = triangle[0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            d[i][j] = triangle[i][j] + d[i-1][j]
        elif j == i:
            d[i][j] = triangle[i][j] + d[i-1][j-1]
        else:
            d[i][j] = triangle[i][j] + max(d[i-1][j-1], d[i-1][j])
print(max(d[n-1]))