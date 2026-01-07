N = int(input())
score = list(map(int,input().split()))
ms = max(score)
print(sum(s / ms * 100 for s in score) / N)
#ss = 0
#for s in score:
#    s = s / ms * 100
#    ss += s
#print(ss/N)