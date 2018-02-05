from settings import SCHOOL_INFO, TEACHER_INFO, STUDENT_INFO, CLASSES_INFO, COURSE_INFO
from tools.db_handler import Mypickle

db_handler = Mypickle()


class Admin:
    # 管理员类
    menu = [
        ['创建校区', 'create_school'],
        ['创建课程', 'create_course'],
        ['创建讲师', 'create_teacher'],
        ['创建班级', 'create_classes'],
        ['创建学员', 'create_student'],
        ['查看校区', 'show_school'],
        ['查看课程', 'show_course'],
        ['查看讲师', 'show_teacher'],
        ['查看班级', 'show_classes'],
        ['查看学员', 'show_student'],
    ]

    def __init__(self, name):
        self.name = name

    def show_school(self):
        school_list = db_handler.show_from_file(SCHOOL_INFO)
        for index, obj in enumerate(school_list):
            print(str(index) + '.', obj)
        return school_list

    def show_course(self):
        course_list = db_handler.show_from_file(COURSE_INFO)
        for index, obj in enumerate(course_list):
            print(str(index) + '.', obj)
        return course_list

    def show_teacher(self):
        teacher_list = db_handler.show_from_file(TEACHER_INFO)
        for index, obj in enumerate(teacher_list):
            print(str(index) + '.', obj)
        return teacher_list

    def show_classes(self):
        class_list = db_handler.show_from_file(CLASSES_INFO)
        for index, obj in enumerate(class_list):
            print(str(index) + '.', obj)
        return class_list

    def show_student(self):
        student_list = db_handler.show_from_file(STUDENT_INFO)
        for index, obj in enumerate(student_list):
            print(str(index) + '.', obj)
        return student_list

    def create_school(self):
        school_name = input('学校名称：')
        school_city = input('校区名称：')
        school_obj = School(school_name, school_city)
        db_handler.dump_to_file(school_obj, SCHOOL_INFO)

    def create_teacher(self):
        school_list = self.show_school()
        choice_school = input('输入校区：')
        teacher_name = input('老师名称：')
        school_list[int(choice_school)].add_teacher(teacher_name)

    def create_classes(self):
        school_list = self.show_school()
        choice_school = input('选择校区：')
        classes_name = input('班级名称：')
        classes_date = input('开班日期')
        teacher_list = self.show_teacher()
        choice_teacher = input('选择讲师：')
        course_list = self.show_course()
        choice_course = input('选择课程：')
        school_list[int(choice_school)].add_classes(classes_name,
                                                    classes_date,
                                                    teacher_list[int(choice_teacher)],
                                                    course_list[int(choice_course)])

    def create_course(self):
        school_list = self.show_school()
        choice_school = input('输入校区：')
        print('正在为%s校区添加课程>>>' % school_list[int(choice_school)])
        course_name = input('课程名：')
        course_period = input('课程周期：')
        course_price = input('课程价格：')
        school_list[int(choice_school)].add_course(course_name, course_period, course_price)

    def create_student(self):
        student_name = input('输入学员：')
        school_list = self.show_school()
        choice_school = input('输入校区：')
        classes_list = self.show_classes()
        choice_classes = input('输入班级：')
        school_list[int(choice_school)].add_student(student_name, classes_list[int(choice_classes)])


class School:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.course = []
        self.classes = []
        self.teacher = []
        self.student = []

    def __str__(self):
        return '<%s  %s校区> ' % (self.name, self.city)

    def add_course(self, course_name, course_period, course_price):
        course_obj = Course(course_name, course_period, course_price)
        self.course.append(course_obj)
        db_handler.dump_to_file(course_obj, COURSE_INFO)
        db_handler.update_to_file(self, SCHOOL_INFO)

    def add_teacher(self, teacher_name):
        teacher_obj = Teacher(teacher_name)
        teacher_obj.school = self
        self.teacher.append(teacher_obj)
        db_handler.dump_to_file(teacher_obj, TEACHER_INFO)
        db_handler.update_to_file(self, SCHOOL_INFO)
        db_handler.save_to_users(teacher_name, role='2')

    def add_classes(self, classes_name, classes_date, teacher_obj, course_obj):
        classes_obj = Classes(classes_name, classes_date)
        classes_obj.teacher = teacher_obj
        classes_obj.course = course_obj
        self.classes.append(classes_obj)
        db_handler.dump_to_file(classes_obj, CLASSES_INFO)
        db_handler.update_to_file(self, SCHOOL_INFO)

    def add_student(self, student_name, classes_obj):
        student_obj = Student(student_name)
        self.student.append(student_obj)
        classes_obj.student.append(student_obj)
        student_obj.classes = classes_obj
        student_obj.school = self
        db_handler.dump_to_file(classes_obj, CLASSES_INFO)
        db_handler.update_to_file(self, SCHOOL_INFO)
        db_handler.dump_to_file(student_obj, STUDENT_INFO)
        db_handler.save_to_users(student_name, role='3')


class Classes:
    def __init__(self, name, classes_date):
        self.name = name
        self.classes_date = classes_date
        self.teacher = None
        self.course = None
        self.student = []

    def __str__(self):
        return '班级:{0} \t开班日期:{1} \t讲师:{2} \t课程:{3} \t学员:{4}'.format(self.name,
                                                                     self.classes_date,
                                                                     self.teacher,
                                                                     self.course.name,
                                                                     [i.user for i in self.student])


class Course:
    def __init__(self, name, period, price):
        self.name = name
        self.period = period
        self.price = price

    def __str__(self):
        return '课程名：%s \t周期：%s \t价格：%s' % (self.name, self.period, self.price)


class Teacher:
    menu = [
        [],
        [],
    ]

    def __init__(self, name):
        self.name = name
        self.school = None

    def __str__(self):
        return '<%s %s>--讲师: %s' % (self.school.name, self.school.city, self.name)


class Student:
    menu = []

    def __init__(self, user):
        self.user = user
        self.school = None
        self.classes = None

    def __str__(self):
        return '学员:%s \t所属学校：%s \t所在班级:%s \t课程:%s' % (self.user,
                                                      self.school.name,
                                                      self.classes.name,
                                                      self.classes.course.name)
