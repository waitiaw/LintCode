import threading
import time


class MyModbus(threading.Thread):
    def __init__(self):
        super().__init__()
        pass

    def run(self):
        while True:
            print('run method')
            time.sleep(1)

    def work_continuously(self):
        while True:
            print('run work_con-')
            time.sleep(1)


m = MyModbus()
t1 = threading.Thread(target=m.run, args=())
t2 = threading.Thread(target=m.work_continuously, args=())
t_array = [t1, t2]
for t in t_array:
    t.start()
print('AAAA')
