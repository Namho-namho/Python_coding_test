import sys
input = sys.stdin.readline

stack = []
K = int(input())
for _ in range(K):
    i = int(input())
    if i != 0:
        stack.append(i)
    else:
        stack.pop()
print(sum(stack))