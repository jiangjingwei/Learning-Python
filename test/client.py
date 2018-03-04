import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_port = ('127.0.0.1', 9999)

s.connect(ip_port)

s.send(b'hello world')

rec = s.recv(1024)

print(rec.decode('utf-8'))