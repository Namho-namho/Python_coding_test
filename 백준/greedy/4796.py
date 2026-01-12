i = 0
while(True):
    L, P, V = map(int, input().split())
    if L == 0 and P == 0  and V == 0:
        break
    else:
        i += 1
        day = (V // P) * L
        day += min(V % P, L) # L이 더 클 수도 있는 상황 고려
        print(f"Case {i}: {day}")