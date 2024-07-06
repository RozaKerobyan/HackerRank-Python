students = []

for i in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

score_marks = sorted(set(score for name, score in students))
second_grade = score_marks[1]
second_student = sorted(set([name for name, score in students if score == second_grade]))

for j in second_student:
    print(j)
