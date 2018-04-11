s = 'user=alex&pwd=123'

username, password = s.split('&')


user = username[5:]
pwd = password[4:]

print(user,pwd)