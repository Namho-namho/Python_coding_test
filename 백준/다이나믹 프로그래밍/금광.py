t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    d = []
    index = 0
    for i in range(n):
        d.append(array[index:index + m])
        index += m
    # d[i][j] = array[i][j] + max(d[i - 1][j - 1], d[i][j - 1], d[i + 1][j - 1])
    for j in range(1, m):
        for i in range(n):
            if i == 0:
                leftup = 0
            else:
                leftup = d[i - 1][j - 1]
            if i == n - 1:
                leftdown = 0
            else:
                leftdown = d[i + 1][j - 1]
            left = d[i][j - 1]
            d[i][j] += max(leftup, leftdown, left)
    result = 0
    for i in range(n):
        result = max(result, d[i][m - 1])
    print(result)