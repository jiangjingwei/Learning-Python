from core import views

def main():
    while True:
        welcome_info = '''
        ------------选课系统首页------------
        1、学员账号登录
        2、老师账号登录
        3、管理员账号登录
        '''
        print(welcome_info)

        actions = {
            '1': 'student_sys',
            '2': 'teacher_sys',
            '3': 'admin_sys',
        }
        choice = input('请选择登录方式：')
        if choice.isdigit() and 0 < int(choice) <= len(actions):
            controller(actions[choice])
        else:
            print('输入有误...')


def controller(system):
    if hasattr(views, system):
        sys = getattr(views, system)
        sys()

main()