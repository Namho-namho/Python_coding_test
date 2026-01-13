# "-"뒤는 묶어서 합침 -> greedy
N = input()
part = list(N.split("-"))  # str.split()은 해당 구분자가 없어도 빈 리스트가 아니라 자기 자신을 담은 리스트 생성
total = sum(map(int, part[0].split("+")))

for i in part[1:]:
    total -= sum(map(int, i.split("+")))

print(total)