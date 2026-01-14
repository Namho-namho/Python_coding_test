N = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))
# 왼쪽부터 지금까지의 최소 주유 가격 유지
min_price = price[0] # -> 이전 값 확인 단순 변수 사용 로직**
total = 0

for i in range(N - 1):
    if price[i] < min_price:
        min_price = price[i]
    total += min_price * distance[i]

print(total)