import math
import backtrader as bt
from backtrader import indicators

class GoldenCross(bt.Strategy):
    params = (('fast',50), ('slow',200), ('order_percentage', 0.95), ('ticker','BTC-USD'))

    # Cross over give = 1 if first data cross second up  (50 crossed 200)
    # Cross over give = -1 if first data cross second down (200 crossed 50)

    def __init__(self):
        self.fast_moving_average = bt.indicators.SimpleMovingAverage(
            self.data.close, period=self.params.fast, plotname= '50 day moving average'
        )

        self.slow_moving_average = bt.indicators.SimpleMovingAverage(
            self.data.close, period=self.params.slow, plotname='200 day moving average'
        )

        self.crossover = bt.indicators.CrossOver(self.fast_moving_average,self.slow_moving_average)


    # buy and sell conditions
    def next(self):
        # buy condition
        # check positions size
        if self.position.size == 0:   # no positions
            if self.crossover > 0:     # 50 crossed 200 = 1
                amount_to_invest = (self.params.order_percentage * self.broker.cash)
                # round size down if we have 100,000 and btc close at 100
                # we will buy 1000 btc
                self.size = math.floor(amount_to_invest / self.data.close)

                # execute order
                print(f"Buy{self.size} {self.params.ticker} at {self.data.close[0]} ")

                self.buy(size=self.size)

        # sell condition
        if self.position.size > 0:
            if self.crossover < 0:
                print(f"Sell {self.size} {self.params.ticker} at {self.data.close[0]} ")

                self.sell(size=self.size)
