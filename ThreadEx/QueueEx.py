import queue
import random
import time
from threading import Thread


def producer(q):
    while True:
        print("Producing")
        item =random.randint(1,50)
        q.put(item)

        print("Produced")
        time.sleep(3)


def consumer(q):
    while True:
        print("Consuming")
        print("Consumed data", q.get())
        time.sleep(3)


q = queue.Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))

t1.start()
t2.start()
