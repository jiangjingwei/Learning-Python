import pymysql
import json


def index(request):
    path = 'templates' + request.get('path')
    f = open(path, 'rb')
    data = f.read()
    # print(data)
    return [data]


def templates(request):
    path = 'templates' + request.get('path')
    # print(path)
    f = open(path, 'rb')
    data = f.read()
    # print(data)
    return [data]


def login(request):
    print('login...', )

    post_data = request.get('data').decode('utf-8')
    username, password = post_data.split('&')
    user = username[5:]
    pwd = password[4:]

    conn = pymysql.connect(host='localhost', user='root', password='', database='test', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    sql = "select * from USER  WHERE username=%s and password=%s"

    result = cursor.execute(sql, [user, pwd])

    data_dict = cursor.fetchall()
    print(data_dict)

    recv_data = {}

    if result:
        recv_data["code"] = 1,
        recv_data["message"] = "登陆成功"
    else:
        recv_data["code"] = 0,
        recv_data["message"] = "用户名或密码错误"

    recv_data = json.dumps(recv_data).encode('utf-8')

    return [recv_data]