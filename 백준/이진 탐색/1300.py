import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

start = 1
end = k # k번째 값이 k보다 클 수 없음
while(start <= end):
    mid = (start + end) // 2
    count = 0
    # mid보다 작아야함 i*j <= mid
    for i in range(1, n+1):
        count += min(n, mid // i) # mid // i가 n보다 클 수도 있음

    if count < k:
        start = mid + 1
    else:
        ans = mid
        end = mid - 1
        
print(ans)