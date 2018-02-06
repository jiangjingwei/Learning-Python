import os
import json
from settings import USERS_PATH


def login():
    username = input('用户名：')
    password = input('密码：')
    with open(USERS_PATH, 'r') as f:
        for item in f:
            user, pwd, role = item.strip().split(',')
            if username == user and password == pwd:
                print('登录成功...')
                return {'user': user, 'role': role}
        else:
            print('登录失败...')



