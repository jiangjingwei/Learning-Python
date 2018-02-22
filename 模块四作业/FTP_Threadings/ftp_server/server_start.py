import sys
import os

from core.server import FTPServer

if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(BASE_DIR)
    server = FTPServer()
    server.run()
