import json
from settings import BASE_DIR, logger_operation


def save_to_file(user_dict):
    ''' 用户信息保存到文件 '''
    user_file = BASE_DIR + '/users/' + user_dict['user_info']['username'] + '.json'
    with open(user_file, 'w') as f:
        f.write(json.dumps(user_dict['user_info']))
    logger_operation.info('save account {0}'.format(user_dict['user_info']['username']))
    exit('退出程序...')
