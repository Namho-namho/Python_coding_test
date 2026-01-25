from collections import deque

N = int(input())
turn = list(map(int, input().split()))
deq = deque(range(1, N + 1))

for _ in range(N):
    d = deq.popleft()
    i = turn[d-1]
    print(d, end=" ")
    if not deq:
        break
    if i < 0:
        for _ in range(-i):
            deq.appendleft(deq.pop())
    elif i > 0:
        for _ in range(i-1):
            deq.append(deq.popleft())