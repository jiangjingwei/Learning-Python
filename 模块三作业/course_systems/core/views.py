from core.models import Admin, Teacher, Student
from settings import SCHOOL_INFO, TEACHER_INFO, STUDENT_INFO, CLASSES_INFO, COURSE_INFO
from tools.db_handler import Mypickle

db_handler = Mypickle()


def student_sys(user):
    student_obj = get_obj(user, STUDENT_INFO)
    controller(student_obj)



def teacher_sys(user):
    teacher_obj = get_obj(user, TEACHER_INFO)
    controller(teacher_obj)


def admin_sys(user):
    admin = Admin(user)
    controller(admin)


def controller(obj):
    while True:
        for index, value in enumerate(obj.menu):
            print(str(index) + '.', value[0])
        choice = input('请输入选项：')
        getattr(obj, obj.menu[int(choice)][1])()


def get_obj(user, filename):
    obj_list = db_handler.show_from_file(filename)
    for obj in obj_list:
        print(obj.name)
        if obj.name == user:
            return obj

