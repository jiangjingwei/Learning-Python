import sys
import os

from core.client import FTPClient

if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(BASE_DIR)
    try:
        client = FTPClient()
    except ConnectionRefusedError:
        exit('请检查ip地址和端口')
    else:
        client.run()