# 3차원 list
W = [[[0]*21 for _ in range(21)] for _ in range(21)]

#bottom up
for a in range(21):
    for b in range(21):
        for c in range(21):
            if a == 0 or b == 0 or c == 0:
                W[a][b][c] = 1
            elif a < b < c:
                W[a][b][c] = W[a][b][c-1] + W[a][b-1][c-1] - W[a][b-1][c]
            else:
                W[a][b][c] = W[a-1][b][c] + W[a-1][b-1][c] + W[a-1][b][c-1] - W[a-1][b-1][c-1]

while(True):
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    if a <= 0 or b <= 0 or c <= 0:
        ww = 1
    elif a > 20 or b > 20 or c > 20:
        ww = W[20][20][20]
    else:
        ww = W[a][b][c]
    print(f"w({a}, {b}, {c}) = {ww}")