class People:
    hometown = 'shanghai'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('正在吃饭')


class Teacher(People):

    def __init__(self, name, age, gongjili):
        super(Teacher, self).__init__(name, age)
        self.gongjili = gongjili

    def teach(self):
        print('%s 讲课。。。' % self.name)

    def homework(self):
        print('%s 布置作业。。。' % self.name)

    def fight(self, s):
        print(s.blood - self.gongjili)


class Student(People):

    def __init__(self, name, age, blood):
        super(Student, self).__init__(name, age)
        self.blood = blood

    def fazhan(self):
        print('%s 罚站。。。' % self.name)