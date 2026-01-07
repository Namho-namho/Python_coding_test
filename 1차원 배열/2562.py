'''data = []
for _ in range(9):
    number = int(input())
    data.append(number)

max_data, max_index = data[0], 1

for i in range(1, 9):
    if data[i] > max_data:
        max_data = data[i]
        max_index = i + 1

print(max_data, max_index, sep="\n")'''

data = [int(input()) for _ in range(9)]

max_data = max(data)
print(max_data)
print(data.index(max_data) + 1)