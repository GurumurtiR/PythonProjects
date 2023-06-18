class student:
    total = 500
    marks = 450

    def __int__(self, marks):
        self.marks = marks
        print("initialized...")
    def find(self):
        return self.total - self.marks
    def findPercentage(self):
        return self.marks/self.total*100

a = student()
print('total marks:', a.total)
print('losses marks:',a.find())
print('percentage:', a.findPercentage())

