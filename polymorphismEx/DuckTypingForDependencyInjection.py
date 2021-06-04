class Flight:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()


class AirBusEngine:
    def start(self):
        print("AirBusEngine Start")


class BoeingEngine:
    def start(self):
        print("BoeingEngine Start")

ae = AirBusEngine()
be = BoeingEngine()
f = Flight(be)
f.start()
