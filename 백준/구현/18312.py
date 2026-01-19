# 완전 탐색
N, K = map(int, input().split())
count = 0

for a in range(N + 1):
    for b in range(60):
        for c in range(60):
            if str(K) in f"{a:02d}{b:02d}{c:02d}": # K가 0일때 고려
                count += 1
print(count)