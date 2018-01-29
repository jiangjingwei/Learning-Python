from settings import BASE_DIR, logger_operation
import os
import json

user_dict = {
    'is_login': False,
    'user_info': None,
    'user_status': 0,
    'user_salary': 0,
    'shopping_car': None,
}


def login(func):
    ''' 用户登录装饰器 '''
    def inner():
        count = 0
        while user_dict['is_login'] is not True and count < 3:
            count += 1
            username = input('请输入用户名：')
            password = input('请输入密码：')
            status = check_user(username, password)
            if status and user_dict['user_status'] == 0:
                print('登录成功！')
                logger_operation.info('login success {0}'.format(user_dict['user_info']['username']))
                func(user_dict)
            elif user_dict['user_status'] == 1:
                print('账号被锁定...')
                logger_operation.warning('account locked {0}'.format(user_dict['user_info']['username']))
            else:
                print('账号或密码错误...')
                logger_operation.warning('account wrong {0}'.format(user_dict['user_info']['username']))

            if count == 3:
                break
    return inner


def check_user(username, password):
    ''' 检查用户名和密码 '''
    user_file = BASE_DIR + '/users/' + username + '.json'
    if os.path.isfile(user_file):
        with open(user_file, 'r') as f:
            user_data = json.loads(f.read())
            if username == user_data['username'] and password == user_data['password']:
                user_dict['is_login'] = True
                user_dict['user_info'] = user_data
                user_dict['user_status'] = user_data['status']
                user_dict['user_salary'] = user_data['credit_card'][0]['salary']
                return True
            else:
                return False
    else:
        return False
