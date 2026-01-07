'''
a = int(input())
b = int(input())
b1 = b%10
b3 = b//100
b2 = (b-b3*100)//10 
a3 = a*b1
a4 = a*b2
a5 = a*b3
a6 = a3 + a4*10 + a5*100
print(a3, a4, a5, a6, sep="\n")
'''
#문자열은 인덱싱 가능
a = int(input())
b = input()

for i in [2, 1, 0]:
    print(a*int(b[i]))

print(a*int(b))