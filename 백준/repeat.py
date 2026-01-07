'''2739
N = int(input())

for i in range (1, 10):
    print(N, "*", i, "=", N*i)
'''
'''10950
T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(A + B)
'''
'''8393
n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i
print(sum)
'''
'''25304
X = int(input())
N = int(input())
sum = 0
for _ in range(N):
    a, b = map(int, input().split())
    sum += a*b
if sum == X:
    print("Yes")
else:
    print("No")
'''
'''25314
N = int(input())
N = N // 4
for _ in range (N):
    print("long", end=" ")
print("int")
###
N = int(input())
print("long "*(N//4) + "int")
'''
'''15552
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)
'''
'''11021
import sys

T = int(sys.stdin.readline())
for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print("Case #{}: {}".format(i + 1, A + B))
'''
'''11022
import sys

T = int(sys.stdin.readline())
for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(f"Case #{i + 1}: {A} + {B} = {A + B}")
'''
'''2438
import sys

N = int(sys.stdin.readline())
for i in range(1, N + 1):
    print("*" * i)
'''
'''2439
import sys

N = int(sys.stdin.readline())
for i in range(1, N + 1):
    print(" " * (N - i) + "*" * i)
'''
'''10952***
import sys
input = sys.stdin.readline

while True:
    A, B = map(int, input().split())
    if A ==0 and B == 0:
        break
    print(A + B)
'''
'''10951
while True:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except EOFError:
        break


| 함수                    | EOF에서         |
| ---------------------- | -------------   |
| `input()`              | `EOFError` 발생 |
| `sys.stdin.readline()` | `""` 반환       |

'''
import sys

for line in sys.stdin:
    A, B = map(int, line.split())
    print(A + B)

# sys.stdin.readline.rstrip()
# sys.stdin.read()
