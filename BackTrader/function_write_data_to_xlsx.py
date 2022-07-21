import xlsxwriter

# get data from trade_list after cerebro run.
########################################################################################################################

colum_names =['ref','ticker','dir','datein','pricein','dateout','priceout','chng%','pnl','pnl%','size','value','cumpnl','nbars','pnl/bar','mfe%','mae%']
# write file
# create file (workbook and worksheet)
outWorkbook = xlsxwriter.Workbook("out2.xlsx")
outSheet = outWorkbook.add_worksheet()

# write data to file
# write colum names
for item in range(len(colum_names)):
    outSheet.write(0,item,colum_names[item])
########################################################################################################################
# write data ref
for data in range(len(trade_list)):
    outSheet.write(data+1,0,trade_list[data]['ref'])
# write data ticker
for data in range(len(trade_list)):
    outSheet.write(data+1,1,trade_list[data]['ticker'])
# write data dir
for data in range(len(trade_list)):
    outSheet.write(data+1,2,trade_list[data]['dir'])
# write data datein
date_format = outWorkbook.add_format({'num_format':'yyyy-mm-dd'}) # set format for data
for data in range(len(trade_list)):
    outSheet.write_datetime(data+1,3,trade_list[data]['datein'],date_format)
# write data pricein
for data in range(len(trade_list)):
    outSheet.write(data+1,4,trade_list[data]['pricein'])
# write data dateout
date_format = outWorkbook.add_format({'num_format':'yyyy-mm-dd'}) # set format for data
for data in range(len(trade_list)):
    outSheet.write_datetime(data+1,5,trade_list[data]['dateout'],date_format)
# write data priceout
for data in range(len(trade_list)):
    outSheet.write(data+1,6,trade_list[data]['priceout'])
# write data chng%
for data in range(len(trade_list)):
    outSheet.write(data+1,7,trade_list[data]['chng%'])
# write data pnl
for data in range(len(trade_list)):
    outSheet.write(data+1,8,trade_list[data]['pnl'])
# write data pnl%
for data in range(len(trade_list)):
    outSheet.write(data+1,9,trade_list[data]['pnl%'])
# write data size
for data in range(len(trade_list)):
    outSheet.write(data+1,10,trade_list[data]['size'])
# write data value
for data in range(len(trade_list)):
    outSheet.write(data+1,11,trade_list[data]['value'])
# write data cumpnl
for data in range(len(trade_list)):
    outSheet.write(data+1,12,trade_list[data]['cumpnl'])
# write data nbars
for data in range(len(trade_list)):
    outSheet.write(data+1,13,trade_list[data]['nbars'])
# write data pnl/bar
for data in range(len(trade_list)):
    outSheet.write(data+1,14,trade_list[data]['pnl/bar'])
# write data mfe%
for data in range(len(trade_list)):
    outSheet.write(data+1,15,trade_list[data]['mfe%'])
# write data mae%
for data in range(len(trade_list)):
    outSheet.write(data+1,16,trade_list[data]['mae%'])


########################################################################################################################
# close file
outWorkbook.close()