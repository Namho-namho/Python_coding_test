import sys
input = sys.stdin.readline
import heapq

t = int(input())
for _ in range(t):
    k = int(input())
    file = list(map(int, input().split()))
    #우선순위 큐 -> 가장 작은 값을 가장 빨리 뽑음
    heapq.heapify(file)
    total = 0

    while(len(file) > 1):
        a = heapq.heappop(file)
        b = heapq.heappop(file)
        c = a + b
        total += c
        heapq.heappush(file, c)
    print(total)

    '''
    add = []
    while len(file) > 1:
        file = sorted(file, reverse= True)
        a = file.pop()
        b = file.pop()
        add.append(a + b)
        file.append(a + b)
    print(sum(add))
    '''