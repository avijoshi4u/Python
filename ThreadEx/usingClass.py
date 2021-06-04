from threading import *


class MyThread:
    def display(self):
        i = 0
        while i <= 10:
            print(i)
            i += 1


mt = MyThread()
t = Thread(target=mt.display())
t.start()
