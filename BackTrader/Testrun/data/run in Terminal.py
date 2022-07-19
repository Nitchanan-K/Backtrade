import os, sys, argparse
import pandas as pd
import backtrader as bt
import matplotlib
matplotlib.use('TKAgg')

# import strategies
from Strategies.buyandhold import BuyHold

from Strategies.goldencross import GoldenCross




# parser use tp run in Terminal
strategies = {
    'golden_cross': GoldenCross,
    'buy_hold': BuyHold
}

parser = argparse.ArgumentParser()
parser.add_argument("strategy", help='which strategy to run', type=str)
args = parser.parse_args()

if not args.strategy in strategies:
    print(f'invalid strategy, must be one in format{strategies.keys()}')
    sys.exit()



#######################################################################################################################

cerebro = bt.Cerebro()
cerebro.broker.setcash(100000)

btc_prices = pd.read_csv('BTC-USD.csv', index_col='Date', parse_dates=True)

feed = bt.feeds.PandasData(dataname=btc_prices)
cerebro.adddata(feed)
cerebro.addstrategy(strategies[args.strategy])
cerebro.run()
cerebro.plot()

