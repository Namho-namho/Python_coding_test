import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()

low = 1
high = house[-1] - house[0]
answer = 0

# 1 2 4 8 9 
while(low <= high):
    # mid : 공유기 최소 간격
    mid = (low + high) // 2
    count = 1
    last = house[0]
    for i in range(1, n):
        if house[i] - last >= mid: # mid보다 크거나 같으면 설치
            count += 1
            last = house[i]

    if count >= c:
        low = mid + 1
        answer = mid
    else:
        high = mid - 1
print(answer)