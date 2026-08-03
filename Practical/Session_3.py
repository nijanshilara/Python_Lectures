# Solution 1: Find the common elements between two sets

first_collection = []
first_count = int(input("Enter the number of elements in the first set: "))

for i in range(first_count):
    value = input("Enter an element for the first set: ")
    first_collection.append(value)

second_collection = []
second_count = int(input("Enter the number of elements in the second set: "))

for j in range(second_count):
    value = input("Enter an element for the second set: ")
    second_collection.append(value)

first_collection = set(first_collection)
second_collection = set(second_collection)

print("First set:", first_collection)
print("Second set:", second_collection)
print("Common elements:", first_collection & second_collection)


# Solution 2: Store student grades and find the highest scorer

grade_record = {}

for index in range(5):
    student_name = input("Enter student name: ")
    student_grade = input("Enter student grade: ")
    grade_record[student_name] = student_grade

highest_student = max(grade_record, key=grade_record.get)

print(
    "The student with the highest grade is:",
    highest_student,
    "with grade:",
    grade_record[highest_student]
)