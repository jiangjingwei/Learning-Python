import sys
import os
from bin.client_server import Client


def main():
    c = Client()
    c.run()


if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(BASE_DIR)
    main()

