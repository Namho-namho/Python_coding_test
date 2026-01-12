N = int(input())
meet = [list(map(int, input().split())) for _ in range(N)]
meet = sorted(meet, key = lambda x:(x[1], x[0]))
# key = (A, B) -> A기준으로 먼저 정렬, A가 같으면 B기준으로 정렬
count = 0
last = 0 # 이전값 확인할때 단순 변수로 확인하는 로직**

# 끝나는 시간이 제일 빠른 순으로 정렬이므로 끝나는 시간과 가장 가까운 시작 시간을 선택
for i in meet:
    if i[0] >= last:
        count += 1
        last = i[1]

print(count)