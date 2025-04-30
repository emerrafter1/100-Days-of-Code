student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))


scores = [8, 65, 89, 86, 55, 91, 64, 89]

max_score = scores[0]

for score in scores:
    if score > max_score:
        max_score=score

max_student_score = student_scores[0]

for score in student_scores:
    if score > max_student_score:
        max_student_score=score


print(max_score)
print(max_student_score)