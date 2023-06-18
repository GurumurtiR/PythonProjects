# inheritance
class Elon:
    def __init__(self):
        print("profile created")

    def name(self):
        print("Elon Musk")

    def age(self):
        print(40)

class spacex(Elon):
    def __init__(self):
        Elon.__init__(self)
        print("company profile created")

    def name(self):
        print("spacex")

    def type(self):
         print("private space travel")

a = spacex()
a.name()
a.age()
