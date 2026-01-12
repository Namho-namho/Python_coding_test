S = input()
result = int(S[0]) # 첫번째 문자를 숫자로 변경하여 대입

for i in range(1, len(S)):
    num = int(S[i])
    # 두 수 중에서 하나라도 0 또는 1인 경우, 더하기 수행
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)