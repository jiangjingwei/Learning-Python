import os
import sys
from core.ftp_server import FtpServer


def main():
    ftp_server = FtpServer()
    ftp_server.start()


if __name__ == '__main__':
    main()
