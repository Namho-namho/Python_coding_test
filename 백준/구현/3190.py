from collections import deque

n = int(input()) # 보드 크기
k = int(input()) # 사과 개수
apple = [] # 사과 위치
for _ in range(k):
    a, b= map(int, input().split())
    apple.append((a-1, b-1))
l = int(input()) 
l_info = deque() # 방향 변환 정보
for _ in range(l):
    a, b = input().split()
    a = int(a)
    l_info.append((a, b))
count = 0 # 초
direction = 0 # 방향
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

headx, heady = 0, 0
snake = deque([(headx, heady)])
while(True):
    count += 1
    headx += dx[direction]
    heady += dy[direction]

    if headx < 0 or heady < 0 or headx >= n or heady >= n:
        break

    if (headx, heady) in snake:
        break

    if (headx, heady) in apple:
        apple.remove((headx, heady))
    else:
        snake.popleft()

    snake.append((headx, heady))

    if l_info and (count == l_info[0][0]):
        _, ly = l_info.popleft()
        if ly == "D":
            direction = (direction + 1) % 4
        else:
            direction = (direction + 3) % 4
        
print(count)