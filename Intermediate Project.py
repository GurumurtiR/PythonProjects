# INTERMEDIATE PROJECT
# STUDENT MANAGEMENT SYSTEM

student_1 = {
    "maths": 45,
    "social": 98,
    "science": 96,
    "name": "radha"
}
student_2 = {
    "maths": 74,
    "social": 83,
    "science": 100,
    "name": "deeraj"
}
student_3 = {
    "maths": 98,
    "social": 96,
    "science": 90 ,
    "name": "sooraj"
}
student_list = [student_1, student_2, student_3]
highest_score_in_maths = 0
highest_score_in_maths_name = " "
highest_score_in_social = 0
highest_score_in_social_name = " "
highest_score_in_science = 0
highest_score_in_science_name = " "
for student in student_list:
    if student.get("maths") > highest_score_in_maths:
        highest_score_in_maths = student.get("maths")
        highest_score_in_maths_name = student.get("name")
print(f"The highest score in maths is {highest_score_in_maths} by {highest_score_in_maths_name}")
for student in student_list:
    if student.get("social") > highest_score_in_social:
        highest_score_in_social = student.get("social")
        highest_score_in_social_name = student.get("name")
print(f"The highest score in social is {highest_score_in_social} by {highest_score_in_social_name}")
for student in student_list:
    if student.get("science") > highest_score_in_science:
        highest_score_in_science = student.get("science")
        highest_score_in_science_name = student.get("name")
print(f"The highest score in science is {highest_score_in_science} by {highest_score_in_science_name}")