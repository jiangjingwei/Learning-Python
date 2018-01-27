from settings import BASE_DIR
import os

user_date = {
    'is_login': False,
    'user_info': None,
}


def login(func):

    def inner():
        while user_date['is_login'] is not True:
            username = input('请输入用户名：')
            password = input('请输入密码：')
            check_user(username, password)
        func()
    return inner


def check_user(username, password):

    user_file = os.path.join(BASE_DIR)
    print(user_file)