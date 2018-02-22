import time
import random
from multiprocessing import Process


class Func(Process):
    def __init__(self, name):
        super(Func, self).__init__()
        self.name = name

    def run(self):
        print('{0} is happing'.format(self.name))
        time.sleep(random.randrange(1, 5))
        print('{0} is ending'.format(self.name))


if __name__ == '__main__':
    p1 = Func('alex')
    p2 = Func('jack')
    p3 = Func('tom')
    p4 = Func('egon')

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    print('主进程')