def solution(n, l, r):
    def kant(i):
        while(i > 0): 
            if i % 5 == 2: # 인덱스가 중앙이면 0
                return False
            i //= 5 # 인덱스가 중앙이 아니더라도 큰 묶음 기준 가운데일 수 있음
        return True
        
    answer = 0
        
    for i in range(l - 1, r):
        if kant(i):
            answer += 1
                
    return answer