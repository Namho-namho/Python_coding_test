'''student = [int(input()) for _ in range(28)]
no_assign = []
for i in range(1, 31):
    if i not in student:
        no_assign.append(i)
print(no_assign[0], no_assign[1], sep='\n')'''
student = {int(input()) for _ in range(28)}

for i in range(1, 31):
    if i not in student:
        print(i)
