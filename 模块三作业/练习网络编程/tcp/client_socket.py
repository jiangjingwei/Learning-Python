import socket
import struct
import json
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_port = ('127.0.0.1', 9999)
s.connect(ip_port)


while True:
    cmd = input('>>>').strip()
    if len(cmd) == 0: continue
    if cmd == 'q': break
    s.send(cmd.encode('utf-8'))

    header_len_bytes = s.recv(4)
    header_length = struct.unpack('i', header_len_bytes)[0]
    header_bytes = s.recv(header_length)
    header = json.loads(header_bytes)
    data_size = header['file_size']

    recv_size = 0
    recv_data = b''
    while recv_size < data_size:
        recv_data += s.recv(1024)
        recv_size += len(recv_data)

    print(recv_data.decode('gbk'))