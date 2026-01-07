S = input()
#for i in 'abcdefghijklmnopqrstuvwxyz':
#    print(S.find(i), end=' ')

print(*(S.find(i) for i in 'abcdefghijklmnopqrstuvwxyz'))

#for i in range(ord('a'), ord('z') + 1):
#    try:
#        print(S.index(chr(i)), end=' ')
#    except:
#        print(-1, end=' ')