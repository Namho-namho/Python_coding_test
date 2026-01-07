'''word = input()
total = 0
i = 0
Croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
while(i < len(word)):
    if word[i:i+2] in Croatia:
        total += 1
        i += 2
    elif word[i:i+3] in Croatia:
        total += 1
        i += 3
    else:
        total += 1
        i += 1
print(total)'''

word = input()
Croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for i in Croatia:
    word = word.replace(i, "*")
print(len(word))