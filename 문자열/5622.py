dial = input()
groups = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
total = 0
for i in dial:
    for t, d in enumerate(groups, start = 3):
        if i in d:
            total += t
            break
print(total)