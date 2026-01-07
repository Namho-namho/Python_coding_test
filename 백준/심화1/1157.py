#word =input().upper()
#wordlen = {}
#for i in word:
#    if i not in wordlen:
#        wordlen[i] = 1
#    else:
#        wordlen[i] += 1
#best = 0
#b = ""
#for key in wordlen:
#    if wordlen[key] > best:
#        best = wordlen[key]
#        b = key
#    elif wordlen[key] == best:
#        best = 1000001
#if best == 1000001:
#    print("?")
#else:
#    print(b)
from collections import Counter

word = input().upper()
counter = Counter(word)

mvalue = max(counter.values())
#mlist = [key for key, value in counter.items() if value == mvalue]
mlist = [key for key in counter if counter[key] == mvalue]

print(mlist[0] if len(mlist) == 1 else "?")