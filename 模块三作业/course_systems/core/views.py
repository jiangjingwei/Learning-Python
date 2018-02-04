from .auth import login
from .models import School

school_info = {
    'school_obj': [],
    'courses': [],
    'classes': [],

}

@login
def student_sys():
    welcome_info = '''
    ------------选课系统（学员）---------
    1、选择课程
    2、
    
    '''
    print('学生系统')

@login
def teacher_sys():
    print('老师系统')

@login
def admin_sys():
    welcome_info = '''
        ------------选课系统 （管理员）---------
        1、创建学校
        2、创建课程
        3、创建班级
        4、创建老师
        '''
    actions = {
        '1': create_school,
        '2': create_course,
        '3': create_class,
        '4': create_teacher,
    }

    choice = input('请输入选项：')
    if choice.isdigit() and 0 < int(choice) <= len(actions):
        actions[choice]()
    else:
        print('输入有误...')
    course_name = input('课程名称：')
    print(welcome_info)

def create_school():
    school_name = input('学校名称：')
    school_city = input('城市：')
    school = School(school_name, school_city)
    school_info['school_obj'].append(school)

def create_course():
    pass

def create_class():
    pass

def create_teacher():
    pass