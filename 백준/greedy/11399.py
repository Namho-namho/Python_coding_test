N = int(input())
P = list(map(int, input().split())) # ~.split()는 None 반환 
P = sorted(P)
total = 0
totalat = 0

for i in P:
    totalat += i
    total += totalat

print(total)