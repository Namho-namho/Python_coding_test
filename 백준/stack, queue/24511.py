from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

queuestack = deque()
# 문제 logic상 stack은 필요없음
for i in range(N):
    if A[i] == 0:
        queuestack.append(B[i])

for i in C:
    if queuestack:
        queuestack.appendleft(i)
        print(queuestack.pop(), end=" ")
    # 예외 처리 -> queue가 없을 때
    else:
        print(i, end=" ")