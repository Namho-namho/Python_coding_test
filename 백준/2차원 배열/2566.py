array2 = [list(map(int, input().split())) for _ in range(9)]
maxval = [-1, 1, 1]
for i in range(9):
    if max(array2[i]) > maxval[0]:
        maxval[0] = max(array2[i])
        maxval[1] = i + 1
        maxval[2] = array2[i].index(maxval[0]) + 1
print(maxval[0])
print(maxval[1], maxval[2])