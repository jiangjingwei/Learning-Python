import queue
from threading import Thread


class MyThreadPool:
    '''自定义线程池'''

    def __init__(self, max_works=1):
        self.max_works = max_works  # 最大线程池个数
        self.task_q = queue.Queue()  # 任务队列

    def submit(self, func, *args, **kwargs):
        '''提交任务'''
        w = (func, args, kwargs)
        self.task_q.put(w)
        self.run()

    def run(self):
        '''获取任务并执行'''
        while not self.task_q.empty():
            task, args, kwargs = self.task_q.get()
            t_list = []
            for i in range(self.max_works):
                t = Thread(target=task, args=args, kwargs=kwargs)
                t.start()

            for k in t_list:
                k.join()




