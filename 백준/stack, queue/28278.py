import sys
input = sys.stdin.readline
stack = []
N = int(input())

for _ in range(N):
    cmd = input().split()

    if cmd[0] == '1':
        stack.append(int(cmd[1]))
    elif cmd[0] == '2':
        #stack.pop() -> 마지막 요소를 제거하고 반환
        #if stack -> 하나라도 있으면 True
        print(stack.pop() if stack else -1) 
    elif cmd[0] == '3':
        print(len(stack))
    elif cmd[0] == '4':
        print(0 if stack else 1)
    elif cmd[0] == '5':
        print(stack[-1] if stack else -1)