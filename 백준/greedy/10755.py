import sys
input = sys.stdin.readline

g = int(input())
p = int(input())

place = list(i for i in range(g+1))

#place[can_gate] = find(can_gate-1) 이걸 통해 place 위치 할당
def find(x):
    if place[x] != x:
        place[x] = find(place[x])
    return place[x]
total = 0

for _ in range(p):
    gate = int(input())
    can_gate = find(gate)

    if can_gate == 0:
        break
    total += 1
    place[can_gate] = find(can_gate-1)

print(total)