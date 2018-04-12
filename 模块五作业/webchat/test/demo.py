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


f = open(r"G:\PycharmProject\Learning-Python\模块五作业\webchat\webChatServer\templates\index.html", 'r', encoding='utf-8')
print(f.read())