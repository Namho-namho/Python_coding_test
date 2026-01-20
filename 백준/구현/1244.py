N = int(input())
switch = list(map(int, input().split()))
sN = int(input())

for _ in range(sN):
    sex, num = map(int, input().split())
    if sex == 1:
        for i in range(N):
            if (i+1) % num == 0:
                switch[i] = (switch[i] + 1)%2
    elif sex == 2:
        switch[num-1] = (switch[num-1] + 1)%2
        k = 1
        while(num - k >= 1 and num + k <= N and switch[num - 1 - k] == switch[num - 1 + k]):
            switch[num - 1 - k] = (switch[num - 1 - k] + 1)%2
            switch[num - 1 + k] = (switch[num - 1 + k] + 1)%2
            k += 1
for i in range(N):
    print(switch[i], end = ' ')
    if (i + 1)%20 == 0:
        print()