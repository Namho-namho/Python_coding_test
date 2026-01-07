piece = list(map(int, input().split()))
realPiece = [1, 1, 2, 2, 2, 8]
print(*(r - p for r,p in zip(realPiece, piece)))
#print(*(realPiece[i]-piece[i] for i in range(len(piece))))