import threading
from threading import Thread


def displayNumbers():
    i = 0
    print("Thread: ", threading.currentThread().getName())
    while i <= 10:
        print(i)
        i += 1


print("Main Thread: ", threading.currentThread().getName())
t = Thread(target=displayNumbers)
t.start()
