'''from collections import Counter
N = int(input())
total = 0
for _ in range(N):
    word = input()
    counter = Counter(word)
    multi = [key for key in counter if counter[key] > 1]
    m = True
    for i in multi:
        a = []
        for wi, w in  enumerate(word):
            if w == i:
                a.append(wi)
        for ii in range(len(a)-1):
            if a[ii]+1 == a[ii+1]:
                continue
            else: 
                m = False
                break
    if m:
        total += 1
print(total)'''
N = int(input())
total = 0
for _ in range(N):
    word = input()
    seen = set()
    previous = ""
    ok = True

    for w in word:
        if w != previous:
            if w in seen:
                ok = False
            seen.add(w)
            previous = w

    if ok:
        total += 1

print(total)