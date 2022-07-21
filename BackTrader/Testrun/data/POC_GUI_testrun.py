import pandas as pd
import backtrader as bt
import matplotlib
matplotlib.use('TKAgg')
from tabulate import tabulate

# import GUI
from tkinter import *
from tkinter import messagebox

# import strategies that in the dict contain stg
from Strategies.buyandhold import BuyHold
from Strategies.goldencross import GoldenCross

# import analyzer
from close_trade_list import trade_list



########################################################################################################################
# backtrader
# set framework
cerebro = bt.Cerebro()
# set cash
cerebro.broker.setcash(10000)
# data
btc_prices = pd.read_csv('BTC-USD.csv', index_col='Date', parse_dates=True)
# feed data and add data
feed = bt.feeds.PandasData(dataname=btc_prices)
cerebro.adddata(feed)
# pre set strategy
cerebro.addstrategy(GoldenCross)
# add analyzers
cerebro.addanalyzer(trade_list, _name='trade_list')

########################################################################################################################
# GUI
# make window
window = Tk()

# make func for button
def click():
    # run
    strats = cerebro.run(tradehistory=True)

    # get analyzer data
    trade_list = strats[0].analyzers.trade_list.get_analysis()
    print('\n=== close data list analyzer === \n', tabulate(trade_list, headers="keys"))

    # plot is last / print any is before plot
    cerebro.plot()

# make save file to xlsx
def save_file_xlsx():
    # run
    strats = cerebro.run(tradehistory=True)
    # get analyzer data
    trade_list = strats[0].analyzers.trade_list.get_analysis()


# make button
button = Button(master=window,
                text="click me!",
                command=click,
                font=('Comic Sans',30),
                foreground="#00FF00",
                background="black",
                activeforeground="#00FF00",
                activebackground="black",
                state = ACTIVE # can be DISABLE
                )

# place button
button.pack()
#run button
window.mainloop()