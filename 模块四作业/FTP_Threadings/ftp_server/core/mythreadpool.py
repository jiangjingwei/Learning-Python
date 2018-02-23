import queue
from threading import Thread



class MyThreadPool:
    '''自定义线程池'''

    def __init__(self, max_works=1):
        self.thread_q = queue.Queue(max_works)  # 线程队列

    def create_thread(self, func, conn):
        '''创建线程并添加到队列'''
        t = Thread(target=func, args=(conn,))
        t.start()
        self.thread_q.put(t)

    def submit(self, func, conn):
        '''提交任务'''
        if not self.thread_q.full():
            self.create_thread(func, conn)