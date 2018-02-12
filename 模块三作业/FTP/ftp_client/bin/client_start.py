import socket
import struct
import json

def main():
    while True:
        client_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_server.connect(('127.0.0.1', 8881))
        username = input('用户名：')
        if not username: break
        client_server.send(username.encode('utf-8'))
        password = input('密码：')
        if not username: break
        client_server.send(password.encode('utf-8'))
        login_status = client_server.recv(1024)
        print()
        if login_status.decode('utf-8') == 'True':
            print('登录成功...')
            while True:
                cmd = input('请输入命令：')
                if not cmd: continue
                client_server.send(cmd.encode('utf-8'))
                if cmd.startswith() == 'get':
                    get(client_server)
                header_length = client_server.recv(4)
                header_json_length = struct.unpack('i', header_length)[0]

                header_info = json.loads(client_server.recv(header_json_length).decode('utf-8'))
                data_size = header_info['data_size']

                recv_size = 0
                recv_data = b''
                while recv_size < data_size:
                    recv_data += client_server.recv(1024)
                    recv_size += len(recv_data)

                print(recv_data.decode('utf-8'))
        else:
            print('登录失败...')


def get(client_server):
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

            recv_size += len(recv_data)

        print(recv_data.decode('utf-8'))



if __name__ == '__main__':
    main()