import socket
import struct
import json
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


ip_port = ('127.0.0.1', 9999)
s.bind(ip_port)
s.listen(5)

while True:
    print('starting....')
    conn, addr = s.accept()
    print('客户端地址：', addr)
    while True:
        cmd = conn.recv(1024)
        print('接受到的命令', cmd)
        obj = subprocess.Popen(cmd.decode('utf-8'),
                               shell=True,
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)

        stdout = obj.stdout.read()
        stderr = obj.stderr.read()

        header = {
            'filename': 'a.text',
            'file_size': len(stdout + stderr),
            'md5': '',
        }

        header_bytes = json.dumps(header).encode('utf-8')
        header_bytes_len = struct.pack('i', len(header_bytes))

        print('命令结果的长度', len(stdout))
        conn.send(header_bytes_len)
        conn.send(header_bytes)
        conn.sendall(stdout + stderr)





