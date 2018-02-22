import time
import random
from multiprocessing import Process


def func(name):
    print('{0} is happing'.format(name))
    time.sleep(random.randrange(1, 5))
    print('{0} is ending'.format(name))


if __name__ == '__main__':
    p1 = Process(target=func, args=('alex',))
    p2 = Process(target=func, args=('jack',))
    p3 = Process(target=func, args=('tom',))
    p4 = Process(target=func, args=('egon',))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    print('主进程')