n = int(input())
weight = {}
num = 9
total = 0

for _ in range(n):
    word = input()
    l = len(word)

    for i in range(l):
        value = 10**(l - i - 1)
        j = word[i]

        if j in weight:
            weight[j] += value
        else:
            weight[j] = value
    
# d.values() : value만 꺼낸 list
w = sorted(weight.values(), reverse=True)

for i in w:
    total += i * num
    num -= 1


print(total)