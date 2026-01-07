T = int(input())
for _ in range(T):
    R, S = input().split()
    R = int(R)
    print(''.join(i * R for i in S))
    #print(*(i * R for i in S), sep = '')