import json
import hashlib
from conf.settings import BASE_DIR


def load_users():
    users_path = BASE_DIR + '/db/users'
    with open(users_path, 'r') as f:
        user_dict = json.loads(f.read())
    return user_dict


def login(username, password):
    username = username.decode('utf-8')
    password = password.decode('utf-8')
    m = hashlib.md5()
    m.update(password.encode('utf-8'))
    passwd_md5 = m.hexdigest()
    users_dict = load_users()
    if username in users_dict:
        if users_dict[username]['passwd'] == passwd_md5:
            return {
                'username': username,
                'home_path': '%s/home/%s' % (BASE_DIR, username),
                'disk_size': '',
            }
        return False
    return False
