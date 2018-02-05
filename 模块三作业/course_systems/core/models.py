from settings import SCHOOL_INFO, TEACHER_INFO, STUDENT_INFO, CLASSES_INFO
from core import mypickle

class Admin:
    # 管理员类
    menu = [
        ['创建校区', 'create_school'],
        ['创建课程', 'create_course'],
        ['创建班级', 'create_classes'],
        ['创建讲师', 'create_teacher'],
    ]

    def __init__(self, name):
        self.name = name
        self.school_pickle_obj = mypickle.Mypickle(SCHOOL_INFO)
        self.teacher_pickle_obj = mypickle.Mypickle(TEACHER_INFO)
        self.student_pickle_obj = mypickle.Mypickle(STUDENT_INFO)
        self.classes_pickle_obj = mypickle.Mypickle(CLASSES_INFO)

    def check_school(self, school_name, school_city):
        for item_obj in self.school_pickle_obj.load_data():
            if school_name == item_obj.name and school_city == item_obj.city:
                return False
        return True

    def create_school(self):
        school_name = input('学校名称：')
        school_city = input('校区名称：')
        if self.check_school(school_name, school_city):
            school_obj = School(school_name, school_city)
            self.school_pickle_obj.dump_data(school_obj)
        else:
            print('学校已存在...')

    def create_teacher(self):
        teacher_name = input('老师名称：')
        for index, item_obj in enumerate(self.school_pickle_obj.load_data()):
            print(str(index) + '.', item_obj)
        choice = input('请选择校区：')
        school_obj = [item for index, item in enumerate(self.school_pickle_obj.load_data()) if index == int(choice)][0]
        if school_obj.teacher:
            for item in school_obj.teacher:
                if item.name == teacher_name:
                    print('老师已存在...')
        else:

            school_obj.teacher.append(Teacher(teacher_name))
            self.teacher_pickle_obj.dump_data(Teacher(teacher_name))
            self.school_pickle_obj.edit_data(school_obj)



    def create_classes(self):
        classes_name = input('班级名称：')
        classes_date = input('开班日期')

        for index, item_obj in enumerate(self.school_pickle_obj.load_data()):
            print(str(index) + '.', item_obj)
        choice = input('请选择校区：')
        school_obj = [item for index, item in enumerate(self.school_pickle_obj.load_data()) if index == int(choice)][0]
        if school_obj.classes:
            for item in school_obj.classes:
                if item.name == classes_name:
                    print('班级已存在...')

        else:

            school_obj.classes.append(Classes(classes_name, classes_date))
            self.school_pickle_obj.edit_data(school_obj)

        for index, item_obj in enumerate(self.teacher_pickle_obj.load_data()):
            print(str(index) + '.', item_obj)
        choice = input('请选择老师：')


    def create_course(self):
        course_name = input('课程名：')
        course_period = input('课程周期：')
        course_price = input('课程价格：')

        for index, item_obj in enumerate(self.school_pickle_obj.load_data()):
            print(str(index) + '.', item_obj)
        choice = input('请选择校区：')
        school_obj = [item for index, item in enumerate(self.school_pickle_obj.load_data()) if index == int(choice)][0]
        if school_obj.course:
            for item in school_obj.course:
                if item.name == course_name:
                    print('课程已存在...')
        else:

            school_obj.course.append(Course(course_name, course_period, course_price))
            self.school_pickle_obj.edit_data(school_obj)


class Teacher:
    def __init__(self, name):
        self.name = name
        self.school = None

    def __str__(self):
        return '%s 校区  %s' % (self.school, self.name)


class School:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.course = []
        self.classes = []
        self.teacher = []
        self.student = []

    def __str__(self):
        return '<%s> <%s校区>' % (self.name, self.city)


class Classes:
    def __init__(self, name, course_date):
        self.name = name
        self.course_date = course_date



class Course:
    def __init__(self, name, period, price):
        self.name = name
        self.period = period
        self.price = price

    def __str__(self):
        return '%s-%s-%s' % (self.name, self.period, self.price)
