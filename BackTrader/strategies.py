import backtrader

class TestStrategy(backtrader.Strategy):

    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close
        # Keep tack of order state
        self.order = None

    # make order object for check status of order
    def notify_order(self, order):
        if order.status in [order.Submitted,order.Accepted]:
            return

        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(f'BUY EXECUTED:{order.executed.price}')
            elif order.issell():
                self.log(f'SELL EXECUTED:{order.executed.price}')

            # track of bar that executed
            self.bar_executed = len(self)

        # after it done
        self.order = None

    def next(self):
        # Simply log the closing price of the series from the reference
        self.log('Close, %.2f' % self.dataclose[0])

        print(len(self))
        #print(self.order)
        #print(self.position)

        # buy condition
        if not self.position:
            if self.dataclose[0] < self.dataclose[-1]:
                # current close less than previous close

                if self.dataclose[-1] < self.dataclose[-2]:
                    # previous close less than the previous close

                    # BUY, BUY, BUY!!! (with all possible default parameters)
                    self.log('BUY CREATE, %.2f' % self.dataclose[0])
                    # make order
                    self.order = self.buy()
        else:
            if len(self) >= (self.bar_executed + 5):
                self.log(f"SELL CREATED: {self.dataclose[0]}")
                self.order = self.sell()