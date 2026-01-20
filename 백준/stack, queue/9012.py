N = int(input())

for _ in range(N):
    data = input()
    stack = []
    vps = True
    for i in data:
        if i == "(":
            stack.append("*")
        elif i == ")":
            if stack:
                stack.pop()
            else:
                print("NO")
                vps = False
                break
    if vps:
        print("NO" if stack else "YES")