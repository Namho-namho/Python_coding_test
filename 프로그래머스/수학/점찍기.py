import math

def solution(k, d):
    answer = 0
    
    for i in range(0, d + 1, k):
        maxy = math.sqrt(d*d - i*i)
        
        numy = maxy//k + 1
        answer += numy
    
    
    return answer