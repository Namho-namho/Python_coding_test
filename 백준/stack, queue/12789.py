N = int(input())
num = map(int, input().split())
low = 1
stack = []

for i in num:
    if i == low:
        low += 1
    else:
        stack.append(i)
    while(stack and stack[-1] == low):
        stack.pop()
        low += 1
print("Nice" if low == N + 1 else "Sad")