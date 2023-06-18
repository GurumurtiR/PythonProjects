class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print('hi', self.name)
        print('total marks:', self.marks)

    def grade(self):
        if self.marks >= 85:
            print('Congradulations, you got distinction')
        elif self.marks >= 60:
            print('you got first class')
        elif self.marks >= 50:
            print('you got second class')
        elif self.marks >= 35:
            print('you got third class')
        else:
            print('Sorry,you are failed')

list_of_student = []

n = int(input('Enter the number of students:'))
for i in range(n):
    name = input('enter student name:')
    marks = int(input('Enter marks:'))
    s = student(name, marks)
    list_of_student.append(s)
    print("students added successfully..")
    option = input('do you want to add one more student[yes/No]:')

    if option.lower() == 'no':
        break

print('All students information..')
for student in list_of_student:
    student.display()
    student.grade()
    print()


