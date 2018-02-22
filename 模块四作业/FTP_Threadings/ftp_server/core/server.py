import socket
import struct
import json
import os
import subprocess
from conf.settings import HOST, PORT, MAX_WORKS, SHARE_DIR
from core.auth import login
from core.mythreadpool import MyThreadPool


class FTPServer:
    '''ftp服务端核心类'''

    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((HOST, PORT))
        self.server_socket.listen(MAX_WORKS)
        self.thread_pool = MyThreadPool(MAX_WORKS)

    def controller(self, conn):
        ''''''
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
                        cmd = cmd.decode('utf-8')
                        func = getattr(self, '_%s' % cmd.split()[0])
                        func(conn, cmd, result)
                else:
                    conn.send('Flase'.encode('utf-8'))
            except:
                break

    def run(self):
        '''启动服务端'''
        print('server starting...')
        while True:
            conn, address = self.server_socket.accept()
            print('客户端：', address)
            self.thread_pool.submit(self.controller, conn)  # 调用线程执行

    def _find(self, conn, cmd, result):
        '''查找文件'''
        if os.name == 'nt':
            find_name = 'dir'
        elif os.name == 'posix':
            find_name = 'ls'
        print(result['home_path'])
        if len(cmd.split()) == 1:
            cmd = '%s %s' % (find_name, result['home_path'])
        else:
            file_path = os.path.join(result['home_path'], cmd.split()[1])
            if os.path.exists(file_path):
                cmd = '%s %s' % (find_name, file_path)
            else:
                cmd = '%s %s' % (find_name, result['home_path'])

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

    def _get(self, conn, cmd, result):
        '''客户端下载文件'''
        filename = cmd.split()[1]

        share_file = os.path.join(SHARE_DIR, filename)

        header = {'filename': filename, 'file_size': None, 'file_status': None}
        if os.path.exists(share_file):
            header['file_status'] = 1
            header['file_size'] = os.path.getsize(share_file)
        else:
            header['file_status'] = 0
        header_bytes = json.dumps(header).encode('utf-8')
        header_length = struct.pack('i', len(header_bytes))
        conn.send(header_length)
        conn.send(header_bytes)

        with open(share_file, 'rb') as f:
            for line in f:
                conn.send(line)

    def _put(self, conn, cmd, result):
        '''上传文件'''
        header_length = conn.recv(4)
        header_json_length = struct.unpack('i', header_length)[0]
        header_info = json.loads(conn.recv(header_json_length).decode('utf-8'))
        data_size = header_info['file_size']
        filename = header_info['filename']
        file_path = '%s/%s' % (result['home_path'], filename)
        with open(file_path, 'wb') as f:
            recv_size = 0
            while recv_size < data_size:
                recv_data = conn.recv(1024)
                f.write(recv_data)
                recv_size += len(recv_data)
