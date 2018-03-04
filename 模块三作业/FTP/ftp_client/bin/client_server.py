import socket
import struct
import json

from conf.settings import HOST, PORT


class Client:
    def __init__(self):
        self.client_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_server.connect((HOST, PORT))

    def login(self):
        while True:
            username = input('用户名：')
            if not username: break
            self.client_server.send(username.encode('utf-8'))
            password = input('密码：')
            if not username: break
            self.client_server.send(password.encode('utf-8'))
            login_status = self.client_server.recv(1024)

            return login_status

    def run(self):
        login_status = self.login()
        print(login_status)
        if login_status.decode('utf-8') == 'True':
            print('登录成功...')
            while True:
                cmd = input('请输入命令：')
                if not cmd: continue
                self.client_server.send(cmd.encode('utf-8'))
                if cmd.startswith('get'):
                    self.get(self.client_server)
                else:
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
        else:
            print('登录失败...')

    def get(self, client_server):
        download_dir = '/Users/eric/PycharmProjects/Learning-Python/模块三作业/FTP/ftp_client/download'
        header_length = client_server.recv(4)
        header_json_length = struct.unpack('i', header_length)[0]

        header_info = json.loads(client_server.recv(header_json_length).decode('utf-8'))
        data_size = header_info['file_size']
        filename = header_info['filename']

        file_path = '%s/%s' % (download_dir, filename)

        with open(file_path, 'wb') as f:
            recv_size = 0
            while recv_size < data_size:
                recv_data = client_server.recv(1024)
                f.write(recv_data)
                recv_size += len(recv_data)
