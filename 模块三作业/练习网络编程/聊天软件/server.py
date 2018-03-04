import socket

ip_port = ('127.0.0.1', 9000)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(ip_port)
s.listen(5)

while True:
    conn, addr = s.accept()
    print('客户端-', addr)
    while True:
        try:
            msg = conn.recv(1024)
            if not msg: break
            print(msg.decode('utf-8'))

            response = input('服务端输入>>>').strip()
            conn.send(response.encode('utf-8'))
        except:
            break
