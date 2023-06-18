#special method
import self as self


class student:
    total = 500

    def __init__(self, name, marks, gender):
        self.name = name
        self.marks = marks
        self.gender = gender
        print("initialized...")

    def __len__(self):
        return self.marks

    def __str__(self):
        return "name: %s | marks: %s | gender: %s" %(self.name, self.marks, self.gender)

    def __del__(self):
        print("student database is deleted")

a = student("champ", 450, 'male')
print(a)
print('marks:', len(a))
del a
