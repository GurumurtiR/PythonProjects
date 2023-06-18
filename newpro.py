class animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def m1(self):
        print('the animal is', self.name)
        print('the animal sound is', self.sound)

    def m2(self):
        print('the animal is', self.name)
        print('the animal sound is', self.sound)


a = animal('dog', 'bow bow')
a.m1()
a = animal('pig', 'wee wee')
a.m2()

