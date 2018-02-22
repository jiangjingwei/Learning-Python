import socket
import json
import struct
import os
from conf.settings import HOST, PORT, DOWNLOAD_DIR


class FTPClient:
    def __init__(self):
        self.client_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_server.connect((HOST, PORT))

    def login(self):
        while True:
            username = input('用户名：').strip()
            if not username: break
            self.client_server.send(username.encode('utf-8'))
            password = input('密码：').strip()
            if not username: break
            self.client_server.send(password.encode('utf-8'))
            login_status = self.client_server.recv(1024)

            return login_status

    def varify_cmd(self, cmd):

        if hasattr(self, '_%s' % cmd.split()[0]):
            func = getattr(self, '_%s' % cmd.split()[0])
            return func
        else:
            return False

    def _find(self, cmd):
        print('查看目录')
        self.client_server.send(cmd.encode('utf-8'))

        header_length = self.client_server.recv(4)

        header_json_length = struct.unpack('i', header_length)[0]

        header_info = json.loads(self.client_server.recv(header_json_length).decode('utf-8'))
        data_size = header_info['data_size']

        recv_size = 0
        recv_data = b''
        while recv_size < data_size:
            recv_data += self.client_server.recv(1024)
            recv_size += len(recv_data)

        print(recv_data.decode('gbk'))

    def _get(self, cmd):
        print('下载文件')
        self.client_server.send(cmd.encode('utf-8'))

        header_length = self.client_server.recv(4)
        header_json_length = struct.unpack('i', header_length)[0]

        header_info = json.loads(self.client_server.recv(header_json_length).decode('utf-8'))

        file_status = header_info['file_status']
        if file_status:
            data_size = header_info['file_size']
            filename = header_info['filename']

            file_path = '%s\%s' % (DOWNLOAD_DIR, filename)

            with open(file_path, 'wb') as f:
                recv_size = 0
                while recv_size < data_size:
                    recv_data = self.client_server.recv(1024)
                    f.write(recv_data)
                    recv_size += len(recv_data)
        else:
            print('文件不存在')

    def _put(self, cmd):
        print('上传文件')
        self.client_server.send(cmd.encode('utf-8'))
        filename = cmd.split()[1]

        dowload_file = os.path.join(DOWNLOAD_DIR, filename)

        if os.path.exists(dowload_file):
            header = {'filename': filename, 'file_size': os.path.getsize(dowload_file)}
            header_bytes = json.dumps(header).encode('utf-8')
            header_length = struct.pack('i', len(header_bytes))

            self.client_server.send(header_length)
            self.client_server.send(header_bytes)

            with open(dowload_file, 'rb') as f:
                for line in f:
                    self.client_server.send(line)
        else:
            print('要上传的文件不存在...')


    def _change(self, cmd):
        print('切换目录')
        self.client_server.send(cmd.encode('utf-8'))


    def run(self):
        while True:
            login_status = self.login()
            print(login_status)
            if login_status.decode('utf-8') == 'True':
                while True:
                    cmd = input('输入命令>>>').strip()
                    if not cmd: continue
                    result = self.varify_cmd(cmd)
                    if result:
                        result(cmd)
                    else:
                        print('命令不存在')
            else:
                print('登陆失败')

