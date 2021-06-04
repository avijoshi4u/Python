from threading import Thread


class Mythread(Thread):
    def run(self):
        i = 0
        while i <= 10:
            print(i)
            i += 1


t = Mythread()
t.start()
