import pandas as pd
import backtrader as bt
import matplotlib
matplotlib.use('TKAgg')
from tabulate import tabulate
# import strategies that in the dict contain stg
from Strategies.buyandhold import BuyHold
from Strategies.goldencross import GoldenCross

# import analyzer
from close_trade_list import trade_list

# dict contain stg
strategies = {
    'golden_cross': GoldenCross,
    'buy_hold': BuyHold
}

# func for stg input
def strategy_input():
    strategy_name = input("ENTER :")
    return cerebro.addstrategy(strategies[strategy_name])


# set framework
cerebro = bt.Cerebro()

# set cash
cerebro.broker.setcash(10000)

# data
btc_prices = pd.read_csv('BTC-USD.csv', index_col='Date', parse_dates=True)

# feed data and add data
feed = bt.feeds.PandasData(dataname=btc_prices)
cerebro.adddata(feed)

# ask for stg input
strategy_input()  # or cerebro.addstrategy(GoldenCross)

# add analyzers
cerebro.addanalyzer(trade_list, _name='trade_list')

# run
strats = cerebro.run(tradehistory=True)

# get analyzer data
trade_list = strats[0].analyzers.trade_list.get_analysis()
print('\n=== close data list analyzer === \n',tabulate(trade_list, headers="keys"))

# plot
cerebro.plot()

