from settings import SCHOOL_INFO, TEACHER_INFO, STUDENT_INFO, CLASSES_INFO, COURSE_INFO
from tools.db_handler import Mypickle

db_handler = Mypickle()


class Admin:
    # 管理员类
    menu = [
        ['创建课程', 'create_course'],
        ['创建讲师', 'create_teacher'],
        ['创建班级', 'create_classes'],
        ['创建学员', 'create_student'],
        ['查看课程', 'show_course'],
        ['查看讲师', 'show_teacher'],
        ['查看班级', 'show_classes'],
        ['查看学员', 'show_student'],
    ]

    def __init__(self, name):
        self.name = name

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
            print(str(index) + '.学员：', obj.name)
        return student_list

    def create_teacher(self):
        while True:
            teacher_name = input('创建讲师名>>>').strip()
            if not teacher_name: continue
            teacher_obj = Teacher(teacher_name)
            db_handler.dump_to_file(teacher_obj, TEACHER_INFO)
            db_handler.save_to_users(teacher_name, role='2')
            print('创建讲师成功', teacher_obj)
            break

    def create_classes(self):
        while True:
            classes_name = input('班级名称：').strip()
            if not classes_name: continue
            classes_date = input('开班日期').strip()
            if not classes_date: continue
            teacher_list = self.show_teacher()
            choice_teacher = input('选择讲师：')
            if not choice_teacher: continue
            if choice_teacher.isdigit():
                if 0 <= int(choice_teacher) <= len(teacher_list) - 1:
                    course_list = self.show_course()
                    choice_course = input('选择课程：')
                    if not choice_course: continue
                    if choice_course.isdigit():
                        if 0 <= int(choice_course) <= len(course_list) - 1:
                            classes_obj = Classes(classes_name, classes_date)
                            classes_obj.teacher = teacher_list[int(choice_teacher)]
                            classes_obj.course = course_list[int(choice_course)]
                            teacher_list[int(choice_teacher)].classes = classes_obj
                            db_handler.dump_to_file(classes_obj, CLASSES_INFO)
                            db_handler.update_to_file(teacher_list[int(choice_teacher)], TEACHER_INFO)
                            print('班级创建成功', classes_obj)
                            break
                        else:
                            print('输入的序号不存在...')

                    else:
                        print('请输入正确的序号...')
                else:
                    print('输入的序号不存在...')
            else:
                print('请输入正确的序号...')

    def create_course(self):
        while True:
            course_name = input('课程名：').strip()
            if not course_name: continue
            course_period = input('课程周期：').strip()
            if not course_period: continue
            course_price = input('课程价格：').strip()
            if not course_price: continue
            course_obj = Course(course_name, course_period, course_price)
            db_handler.dump_to_file(course_obj, COURSE_INFO)
            print('创建课程成功：', course_obj)
            break

    def create_student(self):
        while True:
            student_name = input('输入学员名>>>')
            if not student_name: continue
            student_obj = Student(student_name)
            db_handler.dump_to_file(student_obj, STUDENT_INFO)
            db_handler.save_to_users(student_name, role='3')
            print('创建学员成功', student_obj.name)
            break


class Classes:
    def __init__(self, name, classes_date):
        self.name = name
        self.classes_date = classes_date
        self.teacher = None
        self.course = None
        self.student = []

    def __str__(self):
        info = '''班级:{0} 开班日期:{1} 讲师:{2} 课程:{3} 学员:{4}'''.format(self.name, self.classes_date, self.teacher.name,
                                                                 self.course.name, [i.name for i in self.student])
        return info


class Course:
    def __init__(self, name, period, price):
        self.name = name
        self.period = period
        self.price = price

    def __str__(self):
        return '课程名：%s \t周期：%s \t价格：%s' % (self.name, self.period, self.price)


class Teacher:
    menu = [
        ['上课', 'class_begin'],
        ['打分', 'make_score'],
        ['查看班级', 'check_classes'],

    ]

    def __init__(self, name):
        self.name = name
        self.classes = None
        self.class_begin_records = []

    def __str__(self):
        return '讲师: %s' % self.name

    def class_begin(self):
        while True:
            print('当前上课的班级', self.classes)
            content = input('请输入上课内容大纲：').strip()
            if not content: continue
            if not hasattr(self, 'class_begin_records'):
                self.class_begin_records = []
                self.class_begin_records.append(content)
                print(self.class_begin_records)
            else:
                self.class_begin_records.append(content)
            db_handler.update_to_file(self, TEACHER_INFO)
            break

    def make_score(self):
        flag = True
        while flag:
            if self.classes.student:
                score = input('请输入分数：').strip()
                if not score: continue
                for s in self.classes.student:
                    s.score = score
                    db_handler.update_to_file(s, STUDENT_INFO)
                flag = False
            else:
                print('当前班级没有学员...')
                flag = False

    def check_classes(self):
        print(self.classes)


class Student:
    menu = [
        ['注册', 'register'],
        ['交学费', 'pay_tuition'],
        ['查看个人信息', 'user_info'],
        ['查看班级', 'show_classes'],
    ]

    def __init__(self, name):
        self.name = name
        self.classes = None
        self.pay_money = 0

    def __str__(self):
        if self.classes:
            return '学员:%s \t所在班级:%s \t课程:%s' % (self.name, self.classes.name, self.classes.course.name)
        else:
            return self.name

    def show_classes(self):
        class_list = db_handler.show_from_file(CLASSES_INFO)
        for index, obj in enumerate(class_list):
            print(str(index) + '.', obj)
        return class_list

    def register(self):
        while True:
            self.phone = input('输入手机号：').strip()
            if not self.phone: continue
            if not self.phone.isdigit():
                print('请输入正确的手机号...')
                continue
            if len(self.phone) < 11:
                print('手机号不能少于11位...')
                continue
            self.deposit = input('报名费：').strip()
            if not self.deposit: continue
            if self.deposit.isdigit():
                if float(self.deposit) >= 1000:
                    self.pay_money += 1000
                else:
                    print('定金不能少于1000...')
                    continue
            else:
                print('输入有误...')
                continue
            classes_list = self.show_classes()
            choice_classes = input('选择班级：')
            if not choice_classes: continue
            if choice_classes.isdigit() and 0 <= int(choice_classes) <= len(choice_classes) - 1:
                classes_obj = classes_list[int(choice_classes)]
                self.classes = classes_obj
                classes_obj.teacher.classes = classes_obj
                classes_obj.student.append(self)
                db_handler.update_to_file(self, STUDENT_INFO)
                db_handler.update_to_file(classes_obj, CLASSES_INFO)
                db_handler.update_to_file(classes_obj.teacher, TEACHER_INFO)
                break
            else:
                print('输入有误...')

    def pay_tuition(self):
        if self.pay_money < 19800:
            print('已交定金：', self.pay_money)
            while True:
                money = input('输入剩余缴费金额%s：' % (19800 - self.pay_money))
                if not money: continue
                if money.isdigit() and int(money) >= (19800 - self.pay_money):
                    self.pay_money = int(money) + self.pay_money
                    db_handler.update_to_file(self, STUDENT_INFO)
                    print('缴费成功...')
                    break
                else:
                    print('缴费失败...')
                    continue
        else:
            print('学费已交清，前往班级学习...')

    def user_info(self):
        print(self, '分数：', self.score)
