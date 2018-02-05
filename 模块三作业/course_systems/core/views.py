from core.models import Admin, Teacher

def student_sys():

    print('学生系统...')


def teacher_sys():
    Teacher
    print('老师系统...')


def admin_sys(user):
    admin = Admin(user)
    while True:
        for index, value in enumerate(admin.menu):
            print(str(index) + '.', value[0])
        choice = input('请输入选项：')
        getattr(admin, admin.menu[int(choice)][1])()



