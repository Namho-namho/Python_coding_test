n = input()
room = {}

for i in n:
    if i not in room:
        room[i] = 1
    else:
        room[i] += 1

# dict.get(key) -> key없으면 None, (key, 0) -> key없으면 0
value_6 = room.get('6', 0) + room.get('9', 0)
room['6'] = (value_6+1)//2
room['9'] = 0

print(max(room.values()))
