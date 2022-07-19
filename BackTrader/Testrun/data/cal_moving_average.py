#
closing_price_sum = 0
with open('data/BTC-USD.csv') as f:

    # content = last 200 items from old to new
    content = f.readlines()[-200:]
    for line in content:
        print(line)

        # token
        # make list by use split and split ,
        tokens = line.split(",")
        # str (the close price)
        close = tokens[4]

        closing_price_sum += float(close)

print('\n 200 moving avg is : \n',closing_price_sum / 200)


''' for 50 moving avg
# print('\n 50 moving avg is : \n',closing_price_sum / 50)
# content = f.readlines()[-200:]
'''

