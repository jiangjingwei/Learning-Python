s = 'user=alex&pwd=123'

# username, password = s.split('&')
#
#
# user = username[5:]
# pwd = password[4:]
#
# print(user,pwd)

# s1 = s.replace('=', '||')
#
# print(s1)


# f = open(r"G:\PycharmProject\Learning-Python\模块五作业\webchat\webChatServer\templates\index.html", 'r', encoding='utf-8')
# print(f.read())


# s = '/chat.html/alex'
#
# print(s.split('/', 3))

import pymysql


def message_insert():

    conn = pymysql.connect(host='localhost', user='root', password='', database='test', charset='utf8')
    cursor = conn.cursor()

    insert_message = 'insert into chat_message(sendUser,recvUser,message) VALUES (%s, %s, %s )'

    result = cursor.execute(insert_message, ['alex', 'tom', 'aa'])

    conn.commit()

    conn.close()

    return result


if __name__ == '__main__':
    status = message_insert()
    print(status)