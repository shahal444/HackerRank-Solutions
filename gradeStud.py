def gradingStudents(grades):
    rounded_grades = []
    for grade in grades:
        if grade < 38:
            # If the grade is less than 38, no rounding is needed.
            rounded_grades.append(grade)
        else:
            next_multiple_of_5 = ((grade + 4) // 5) * 5
            if next_multiple_of_5 - grade < 3:
                # If the difference between the next multiple of 5 and the grade is less than 3, round up.
                rounded_grades.append(next_multiple_of_5)
            else:
                # Otherwise, keep the original grade.
                rounded_grades.append(grade)
    return rounded_grades

# Input
grades_count = int(input().strip())
grades = []
for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)

# Call the gradingStudents function
result = gradingStudents(grades)

# Output
for res in result:
    print(res)