import socket
import subprocess

udp_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip_port = ('127.0.0.1', 8888)
udp_s.bind(ip_port)

while True:
    cmd, addr = udp_s.recvfrom(1024)
    print('用户命令---', cmd, addr)

    res = subprocess.Popen(cmd.decode('utf-8'),
                           shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)

    stdout = res.stdout.read()
    stderr = res.stderr.read()

    udp_s.sendto(stdout + stderr, addr)

udp_s.close()