import pymysql
import json

from models import login_check, fetch_all_user, message_insert

LOGIN_STATUS = False


def index(request):
    if LOGIN_STATUS:
        data_dict = fetch_all_user()

        path = 'templates/index.html'
        f = open(path, 'r', encoding='utf-8')

        data = f.read()

        all_item = ''

        for item in data_dict:
            re_item = """<div class="chat-item">
                                <img src="./images/359.jpg" alt="">
                                <div class="item clearfix">
                                    <h3 id="user">%s</h3>
                                    <span class="msg">message</span>
                                    <span class="time">09:12</span>
                                </div>
                            </div>""" % (item['username'])
            all_item += re_item

        # print('all_item', all_item)

        new_data = data.replace("""<div id="chat-item"></div>""", all_item)
        new_data = new_data.encode('utf-8')
        # print('all_item', new_data)

        return [new_data]
    else:

        path = 'templates' + request.get('path')
        f = open(path, 'rb')
        data = f.read()
        # print(data)
        return [data]


def chat(request):
    path = 'templates' + request.get('path')
    # print(path)
    user = request.get('query_string').split('=')[1]

    # print(user)
    f = open(path, 'r', encoding='utf-8')
    data = f.read()
    new_data = data.replace('{{user}}}', user)
    new_data = new_data.encode('utf-8')
    return [new_data]


def templates(request):
    # print(request)
    query_string = request.get('query_string')
    if query_string:
        path = 'templates' + request.get('path')
    else:
        path = 'templates' + request.get('path')
    print(path)
    f = open(path, 'rb')
    data = f.read()

    return [data]


def login(request):
    print('login...', )

    post_data = request.get('data').decode('utf-8')
    username, password = post_data.split('&')
    user = username[5:]
    pwd = password[4:]

    result = login_check(user, pwd)

    data_dict = fetch_all_user()

    # print(data_dict)

    recv_data = {}

    if result:
        global LOGIN_STATUS
        LOGIN_STATUS = True
        recv_data["code"] = 1,
        recv_data["message"] = "登陆成功"
        recv_data['friends'] = data_dict
    else:
        recv_data["code"] = 0,
        recv_data["message"] = "用户名或密码错误"

    recv_data = json.dumps(recv_data).encode('utf-8')

    return [recv_data]


def webchat(request):

    print(request.get('data').decode('utf-8'))

    post_data = request.get('data').decode('utf-8').split('&')

    message_info = {
        'sendUser': None,
        'recvUser': None,
        'message': None
    }

    for item in post_data:
        data = item.split('=')
        if data[0] == 'sendUser':
            message_info['sendUser'] = data[1]

        if data[0] == 'recvUser':
            message_info['recvUser'] = data[1]

        if data[0] == 'message':
            message_info['message'] = data[1]

    status = message_insert(message_info)

    recv_data = {
        "code": 1,
        "message": "发送成功",
    }

    recv_data = json.dumps(recv_data).encode('utf-8')

    return [recv_data]