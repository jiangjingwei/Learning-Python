import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_port= ('127.0.0.1', 9000)
c.connect(ip_port)

while True:
    msg = input('客户端输入>>>')
    if len(msg) == 0: continue
    c.send(msg.encode('utf-8'))

    response = c.recv(1024)
    print(response.decode('utf-8'))