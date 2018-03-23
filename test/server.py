import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_port = ('127.0.0.1', 9999)

s.bind(ip_port)
s.listen(5)

conn, address = s.accept()

data = conn.recv(1024)

conn.send(data)