N = int(input())
for i in range(1, 2*N):
    if i <=N:
        print(" "*(N-i), "*"*(2*i-1), sep="")
    else:
        print(" "*(i-N), "*"*((2*N-i)*2-1), sep="")