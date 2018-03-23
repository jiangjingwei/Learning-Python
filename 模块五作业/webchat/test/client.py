import socket

ip_port = ('127.0.0.1', 8009)

s = socket.socket()
s.connect(ip_port)

while True:
    msg = input('请输入内容>>>:').strip()
    s.send(msg.encode('utf-8'))
    data = s.recv(1024)
    print(str(data, 'utf8'))

s.close()