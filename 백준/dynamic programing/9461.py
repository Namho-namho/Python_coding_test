t = int(input())
# d[1] = 1, 
# d[2] = d[1], d[3] = d[2] ,d[4] = d[1] + d[3], 
# d[5] = d[4] + d[0], d[6] = d[5] + d[1], d[7] = d[6] + d[2], d[8] = d[7] + d[3], d[9] = d[8] + d[4], d[10] = d[9] + d[5], d[11] = d[10] + d[6]
# d[12] = d[11] + d[7]
d = [0] * 101
d[1] = d[2] = d[3] = 1
d[4] = 2
for _ in range(t):
    n = int(input())
    for i in range(5, n + 1):
        d[i] = d[i - 1] + d[i - 5]
    print(d[n])