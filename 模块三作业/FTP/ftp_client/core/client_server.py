import socket
import struct
import json
import sys
import os

from conf.settings import *


def run():
    while True:
        client_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_server.connect(('127.0.0.1', 8881))
        username = input('用户名>>>：')
        if not username: break
        client_server.send(username.encode('utf-8'))
        password = input('密码>>>：')
        if not username: break
        client_server.send(password.encode('utf-8'))
        login_status = client_server.recv(1024)
        if login_status.decode('utf-8') == 'True':
            print('登录成功...')
            while True:
                cmd = input('请输入命令：')
                if not cmd: continue
                actions = {
                    'get': get,
                    'put': put,
                    'ls': check,
                }

                if cmd.split()[0] in actions:
                    client_server.send(cmd.encode('utf-8'))
                    actions[cmd.split()[0]](client_server, cmd)

                else:
                    print('输入的命令不存在...')
                    continue
        else:
            print('登录失败...')


def get(client_server, cmd):
    download_dir = DOWNLOAD_DIR
    header_length = client_server.recv(4)
    header_json_length = struct.unpack('i', header_length)[0]
    header_info = json.loads(client_server.recv(header_json_length).decode('utf-8'))
    print(header_info)
    data_size = header_info['file_size']
    filename = header_info['filename']
    file_path = '%s/%s' % (download_dir, filename)
    with open(file_path, 'wb') as f:
        recv_size = 0
        while recv_size < data_size:
            recv_data = client_server.recv(1024)
            f.write(recv_data)
            recv_size += len(recv_data)
            download_process(recv_size, data_size)


def put(client_server, cmd):
    download_dir = DOWNLOAD_DIR
    filename = cmd.split()[1]
    download_file = '%s/%s' % (download_dir, filename)
    data_size = os.path.getsize(download_file)
    header = {'filename': filename, 'file_size': data_size}
    header_bytes = json.dumps(header).encode('utf-8')
    header_length = struct.pack('i', len(header_bytes))

    client_server.send(header_length)
    client_server.send(header_bytes)

    with open(download_file, 'rb') as f:
        send_size = 0
        for line in f:
            client_server.send(line)
            send_size += len(line)
            download_process(send_size, data_size)


def check(client_server, cmd):
    client_server.send(cmd.encode('utf-8'))
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


def download_process(recv_size, data_size):
    ret = recv_size / data_size
    num = int(ret * 100)
    view = '\r [%-100s]%d%%' % ('#' * num, 100)
    sys.stdout.write(view)
    sys.stdout.flush()
