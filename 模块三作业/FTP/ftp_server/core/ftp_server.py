import socket
import struct
import json
import subprocess
import os

from conf.settings import HOST, PORT, MAX_WORKS
from core.auth import login
from core.mythreadpool import MyThreadPool


class FtpServer:
    '''服务端核心类'''

    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((HOST, PORT))
        self.server_socket.listen(MAX_WORKS)
        self.t_pool = MyThreadPool(MAX_WORKS)

    def start(self):
        '''启动服务端并等待客户端连接'''
        while True:
            print('ftp server starting...')
            conn, addr = self.server_socket.accept()
            self.t_pool.submit(self.run, conn)

    def run(self, conn):
        '''与客户端之间的交互'''
        actions = {
            'ls': self.check,
            'get': self.get,
            'put': self.put,
        }
        while True:
            try:
                username = conn.recv(1024)
                password = conn.recv(1024)
                result = login(username, password)
                if result:
                    conn.send('True'.encode('utf-8'))
                    while True:
                        cmd = conn.recv(1024)
                        if not cmd: break
                        cmd_list = cmd.decode('utf-8').split()
                        if cmd_list[0] in actions:
                            actions[cmd_list[0]](conn, cmd, result)
            except ConnectionResetError:
                break


            else:
                conn.send('False'.encode('utf-8'))

    def check(self, conn, cmd, user_dict):
        '''查看用户家目录'''
        if len(cmd.split()) == 1:
            cmd = 'ls %s' % user_dict['home_path']
        print(cmd)
        obj = subprocess.Popen(cmd,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               shell=True)

        stdout = obj.stdout.read()
        stderr = obj.stderr.read()
        if stderr:
            send_body = stderr
        else:
            send_body = stdout

        header = {'data_size': len(send_body)}
        header_bytes = json.dumps(header).encode('utf-8')
        header_length = struct.pack('i', len(header_bytes))

        conn.send(header_length)
        conn.send(header_bytes)
        conn.sendall(send_body)

    def get(self, conn, cmd, user_dict):
        filename = cmd.decode('utf-8').split()[1]
        share_file = SHARE_DIR + filename

        header = {'filename': filename, 'file_size': os.path.getsize(filename)}
        header_bytes = json.dumps(header).encode('utf-8')
        header_length = struct.pack('i', len(header_bytes))

        conn.send(header_length)
        conn.send(header_bytes)

        with open(share_file, 'rb') as f:
            for line in f:
                conn.send(line)

    def put(self):
        pass
