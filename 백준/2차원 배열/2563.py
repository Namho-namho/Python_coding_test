#mycode -> 3개 이상 겹치면 틀림
N = int(input())
area = 0
arealist = [[0]*2 for _ in range(N)]
for i in range(N):
    A, B = map(int, input().split())
    area += 100
    arealist[i] = [A, B]
for i in range(N - 1):
        for j in range(i+1, N):
            if abs(arealist[i][0] - arealist[j][0]) < 10 and abs(arealist[i][1] - arealist[j][1]) < 10:
                area -= (10 - abs(arealist[i][0] - arealist[j][0])) * (10 - abs(arealist[i][1] - arealist[j][1]))
print(area)

#fixcode -> list에 직접 칠하는 느낌
N = int(input())
area = 0
arealist = [[0]*101 for _ in range(101)]
for _ in range(N):
     A, B = map(int, input().split())
     for i in range(A, A + 10):
          for j in range(B, B + 10):
               arealist[i][j] = 1
for i in range(101):
     for j in range(101):
          if arealist[i][j] == 1:
               area += 1
print(area)