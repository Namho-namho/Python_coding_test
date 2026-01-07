data = [int(input())%42 for _ in range(10)]
dif_data = []
for d in data:
    if d not in dif_data:
        dif_data.append(d)
print(len(dif_data))
#print(len({int(input()) % 42 for _ in range(10)}))