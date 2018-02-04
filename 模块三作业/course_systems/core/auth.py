import os
import pickle
from settings import BASE_DIR

user_dict = {
    'user_info': None,
}


def load_users():
    db_path = BASE_DIR + '/db/'
    users_file = os.path.join(db_path, 'users.text')
    with open(users_file, 'rb') as f:
        data = pickle.loads(f.read())
    return data


def login(func):
    def inner():
        users_list = load_users()
        count = 0
        while True:
            count += 1
            username = input('输入用户名：')
            passwd = input('输入密码：')
            for user in users_list:
                if username == user['username'] and passwd == user['password']:
                    print('登录成功...')
                    user_dict['user_info'] = user
                    func()

            if count == 3:
                exit('退出程序...')
    return inner



