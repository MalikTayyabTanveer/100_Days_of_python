student_score = [100, 200, 145, 380, 450, 120, 670, 430]
#print (max(student_score))

max = 0
for score in student_score:
    if score > max:
        max = score

print(max)
