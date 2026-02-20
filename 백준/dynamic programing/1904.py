import sys
input = sys.stdin.readline
n = int(input())

# 1 -> 1 | 2-> 11,00 | 3 -> 111, 100, 001 | 4 -> 1111, 1100, 1001, 0011, 0000 | 5 -> 11111, 11100, 10000, 00001, 00111, 00100, 11001, 10011

# 메모리 초과
d = [0] * (n+1)
d[1] = 1
if n == 1:
    print(1)
else:
    d[2] = 2
    for i in range(3, n + 1):
        d[i] = d[i-1] + d[i-2]
    print(d[n] % 15746)

# for 백준
if n == 1:
    print(1)
else:
    a, b = 1, 2
    for _ in range(3, n+1):
        a, b = b, (a + b)%15746
    print(b)