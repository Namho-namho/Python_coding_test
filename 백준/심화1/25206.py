import sys
input = sys.stdin.readline
'''grade = [list(input().split()) for _ in range(20)]
score = 0
gradetotal = 0
punglist = list(reversed(["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "*", "F"]))

for a in grade:
    a1 = float(a[1])
    if a[2] in punglist:
        score += a1 * punglist.index(a[2])/2
        gradetotal += a1

print(score/gradetotal if gradetotal > 0 else 0)'''

grade_map = {
    "A+": 4.5, "A0": 4.0,
    "B+": 3.5, "B0": 3.0,
    "C+": 2.5, "C0": 2.0,
    "D+": 1.5, "D0": 1.0,
    "F": 0.0
}
total_score = 0
total_credit = 0

for _ in range(20):
    _, credit, grade = input().split()
    credit = float(credit)

    if grade == "P":
        continue
    total_score += credit * grade_map[grade]
    total_credit += credit
print(total_score/total_credit)