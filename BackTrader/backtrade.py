import matplotlib.pyplot as plt
from matplotlib import dates
import backtrader
import datetime
from matplotlib import warnings
from GoldenCross_stg import GoldenCross
import matplotlib
matplotlib.use('TKAgg')
cerebro = backtrader.Cerebro()

# add money
cerebro.broker.set_cash(100000)

# check money before test strategies
print(f'Starting Portfolio Value:{cerebro.broker.get_value()}')

# make data feed
data = backtrader.feeds.YahooFinanceCSVData(
    dataname= 'BTC-USD.csv')
            # Do not pass values before this date
            #fromdate=datetime.datetime(2021, 7, 18),
            # Do not pass values after this date
            #todate=datetime.datetime(2022, 7, 18),
            #reverse=False)


# connect data
cerebro.adddata(data)

# add strategies
cerebro.addstrategy(GoldenCross)

# add size
cerebro.addsizer(backtrader.sizers.FixedSize, stake= 10)

# run
cerebro.run()

# check money after tested strategies
print(f'Final Portfolio Value:{cerebro.broker.get_value()}')

# plot data
cerebro.plot()