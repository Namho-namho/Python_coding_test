n = 1000 - int(input())
count = 0

while True:
    if n >= 500:
        count += n // 500
        n %= 500
    elif 100 <= n < 500:
        count += n // 100
        n %= 100
    elif 50 <= n < 100:
        count += n // 50
        n %= 50
    elif 10 <= n < 50:
        count += n // 10
        n %= 10
    elif 5 <= n < 10:
        count += n // 5
        n %= 5
    else:
        count += n
        break
print(count)