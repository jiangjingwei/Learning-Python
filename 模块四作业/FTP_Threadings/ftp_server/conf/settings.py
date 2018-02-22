import os
HOST = '127.0.0.1'
PORT = 8001

# 最多支持的线程数
MAX_WORKS = 5

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SHARE_DIR = os.path.join(BASE_DIR, 'share')