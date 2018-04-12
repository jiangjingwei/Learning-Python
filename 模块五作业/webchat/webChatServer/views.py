import pymysql
import json

from models import login_check, fetch_all_user

LOGIN_STATUS = False


def index(request):
    if LOGIN_STATUS:
        data_dict = fetch_all_user()

        path = 'templates/index.html'
        f = open(path, 'r', encoding='utf-8')

        data = f.read()

        all_item = '';

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

        print('all_item', all_item)

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

    f = open(path, 'rb')
    data = f.read()

    return [data]


def templates(request):
    path = 'templates' + request.get('path')

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