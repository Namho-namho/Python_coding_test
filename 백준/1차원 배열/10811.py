N, M = map(int, input().split())
bag = [i + 1 for i in range(N)]
for _ in range(M):
    i, j = map(int, input().split())
    bag[i-1:j] = reversed(bag[i-1:j])
    #l = 0
    #rev_bag = [bag[k] for k in range(j-1, i-2, -1)]
    #for ind in range(i - 1, j):
    #    bag[ind] = rev_bag[l]
    #    l += 1
print(*bag)