from threading import Thread, Lock, Semaphore


class BookMyBus:
    def __init__(self, totalAvailableSeat):
        self.totalAvailableSeat = totalAvailableSeat
        # using lock
        #self.l = Lock()
        # using semaphore
        self.l = Semaphore()
    def buy(self, requestedSeat):
        self.l.acquire()
        print("Available seats are :", self.totalAvailableSeat)
        if self.totalAvailableSeat>= requestedSeat:
            print("Seat requested :", requestedSeat)
            print("Confirming a seat")
            print("processing the payment")
            print("printing the ticket")
            self.totalAvailableSeat-=requestedSeat
        else:
            print("Sorry No seats")
        self.l.release()


obj = BookMyBus(10)

t1 = Thread(target=obj.buy(4,))
t2 = Thread(target=obj.buy(4,))
t3 = Thread(target=obj.buy(5,))

t1.start()
t2.start()
t3.start()
