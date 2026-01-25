from collections import deque
N, K = map(int, input().split())
que = deque(range(1, N + 1))
result = []

for _ in range(N):
    for i in range(K-1):
        que.append(que.popleft())
    result.append(que.popleft())

print("<" + ", ".join(map(str, result)) + ">") # join으로 list사이에 , 넣기