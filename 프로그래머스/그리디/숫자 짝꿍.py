def solution(X, Y):
    list = []
    answer = ""
    
    for i in range(9, -1, -1):
        i = str(i)
        
        count = min(X.count(i), Y.count(i))
        list.append(i * count)
    answer = ''.join(list) # list안의 문자열들을 ''를 사이에 두고 합쳐라
    
    if answer == "":
        return "-1"
    if answer[0] == "0":
        return "0"
    return answer