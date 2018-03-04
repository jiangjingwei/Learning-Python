import socket
import struct
import json
import subprocess
import os

from conf.settings import *
from core.auth import login


def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    actions = {
        'ls': check,
        'get': get,
        'put': put,
    }
    while True:
        print('starting...')
        conn, addr = server_socket.accept()
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
        else:
            conn.send('False'.encode('utf-8'))


def check(conn, cmd, user_dict):
    if len(cmd.split()) == 1:
        cmd = 'ls %s' % user_dict['home_path']

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


def get(conn, cmd, user_dict):
    filename = cmd.decode('utf-8').split()[1]
    share_file = SHARE_DIR + filename
    header = {'filename': filename, 'file_size': os.path.getsize(share_file)}
    header_bytes = json.dumps(header).encode('utf-8')
    header_length = struct.pack('i', len(header_bytes))

    conn.send(header_length)
    conn.send(header_bytes)

    with open(share_file, 'rb') as f:
        for line in f:
            conn.send(line)


def put(conn, cmd, user_dict):

    header_length = conn.recv(4)
    header_json_length = struct.unpack('i', header_length)[0]
    header_info = json.loads(conn.recv(header_json_length).decode('utf-8'))
    data_size = header_info['file_size']
    filename = header_info['filename']

    file_path = '%s/%s' % (user_dict['home_path'], filename)
    with open(file_path, 'wb') as f:
        recv_size = 0
        while recv_size < data_size:
            recv_data = conn.recv(1024)
            f.write(recv_data)
            recv_size += len(recv_data)
