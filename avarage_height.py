student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height
print(f"Total height of all students: {total_height}.")

total_students = 0
for students in student_heights:
    total_students += 1
print(f"Total students: {total_students}.")

avarage_height = round(total_height/total_students, 2)
print(f"The avarage height of all students: {avarage_height}.")