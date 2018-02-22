import socket

udp_c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip_port = ('127.0.0.1', 8888)

while True:
    cmd = input('>>>').strip()
    if len(cmd) == 0: continue

    udp_c.sendto(cmd.encode('utf-8'), ip_port)

    data, addr = udp_c.recvfrom(1024)

    print(data.decode('gbk'))