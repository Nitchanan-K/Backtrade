import backtrader as bt

bt.SIGNAL_LONG

class MyStrategy(bt.Strategy):

    def __init__(self):
        self.sma = bt.SimpleMovingAverage(period=15)

    def next(self):
        if self.sma > self.data.close:
            # do somethings
            pass
        elif self.sma < self.data.close:
            # do somethings
            pass