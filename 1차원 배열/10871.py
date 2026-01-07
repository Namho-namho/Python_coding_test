import sys
input = sys.stdin.readline

N, X = map(int, input().split())
data = map(int, input().split())

print(*(i for i in data if i < X))