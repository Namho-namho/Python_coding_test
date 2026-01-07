'''
N = int(input())
list = map(int, input().split())
v = int(input())
sum = 0

for i in list:
    if i == v:
        sum += 1
print(sum)
'''

import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
v = int(input())

# sum -> count

print(sum(1 for i in data if i == v))