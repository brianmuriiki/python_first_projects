student1 = {
 "name": "Alice",
 "age": 20,
 "grade": "A",
 "marks": 340,
 "form": 4,
 "gender": "Female",
}
student2 = {
 "name": "Bob",
 "age": 22,
 "grade": "B",
 "marks": 280,
 "form": 4,
 "gender": "male",
}
student3 = {
 "name": "kelvin",
 "age": 23,
 "grade": "C+",
 "marks": 150,
 "form": 4,
 "gender": "male",
}
student4 = {
 "name": "lenna",
 "age": 19,
 "grade": "A+",
 "marks": 400,
 "form": 4,
 "gender": "Female",
}
mean_marks = (student1["marks"] + student2["marks"] + student3["marks"] + student4["marks"]) / 4
print("The mean marks of the students is:", mean_marks)
deviation1 = student1["marks"] - mean_marks
deviation2 = student2["marks"] - mean_marks
deviation3 = student3["marks"] - mean_marks
deviation4 = student4["marks"] - mean_marks
print("The deviation of student 1 is:", deviation1)
print("The deviation of student 2 is:", deviation2)
print("The deviation of student 3 is:", deviation3)
print("The deviation of student 4 is:", deviation4)

congression1 = deviation1 ** 2
congression2 = deviation2 ** 2
congression3 = deviation3 ** 2
congression4 = deviation4 ** 2
print("The congression of student 1 is:", congression1)
print("The congression of student 2 is:", congression2)
print("The congression of student 3 is:", congression3)
print("The congression of student 4 is:", congression4)

print("students with marks above the mean:")
if student1["marks"] > mean_marks:
    print(student1["name"])
if student2["marks"] > mean_marks:
    print(student2["name"])
if student3["marks"] > mean_marks:
    print(student3["name"])
if student4["marks"] > mean_marks:
    print(student4["name"])

for student in [student1, student2, student3, student4]:
    print(student["name"], "has marks", student["marks"])