score = 850

if score>100:
    print("enter valid score")
    exit()

if score>=90 and score<100:
    grade = "A"
elif score>=80:
    grade = "B"
elif score>=70:
    grade = "C"
elif score>=60:
    grade = "D"
else:
    grade = "F"

print("Grade: ",grade)