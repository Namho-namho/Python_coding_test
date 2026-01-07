'''1330
a, b = map(int, input().split())
if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")'''
'''
score = int(input())
if  90 <= score <= 100:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 70 <= score < 80:
    print("C")
elif 60 <= score < 70:
    print("D")
else:
    print("F")
'''
'''2753
year = int(input())
if year % 4 == 0:
    if year % 100 !=0 or year % 400 == 0:
        print(1)
    else:
        print(0)
else:
    print(0)
'''
'''14681
x = int(input())
y = int(input())
if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)
'''
'''2884
H, M = map(int, input().split())

if M >= 45:
    print(H, M - 45)
else:
    if H == 0:
        print(23, 60 - abs(M - 45))
    else:
        print(H - 1, 60 - abs(M - 45))
'''
'''2525
A, B = map(int, input().split())
C = int(input())
D = B + C
if D < 60:
    print(A, D)
else:
    if A + D//60 >= 24:
        print(A + D//60 - 24, D%60)
    else:
        print(A + D//60, D%60)
'''
a, b, c = map(int, input().split())
if a == b == c:
    print(10000 + a*1000)
elif a != b and b != c and c != a:
    print(max(a,b,c)*100)
else:
    if a == b:
        print(1000 + a * 100)
    elif b == c:
        print(1000 + b * 100)
    else:
        print(1000 + c * 100)