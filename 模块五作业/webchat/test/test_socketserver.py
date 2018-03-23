import socketserver


class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        print('client address', self.client_address)
        while True:
            try:
                data = self.request.recv(1024)
                if not data: break
                print('client data', data.decode('utf-8'))
                self.request.send(data)
            except Exception:
                self.request.close()


if __name__ == '__main__':
    host_port = ('127.0.0.1', 8009)
    with socketserver.ThreadingTCPServer(host_port, MyServer) as server:
        print('server starting...')
        server.serve_forever()

