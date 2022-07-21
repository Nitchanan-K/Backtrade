import xlsxwriter

# create file (workbook and worksheet)
outWorkbook = xlsxwriter.Workbook("out2.xlsx")
outSheet = outWorkbook.add_worksheet()

# declare data
names = ["TEEe","BOB","KK"]
values = [70,82,90]

outSheet.write("A1","Name")
outSheet.write("B1","Scores")

#write data to file
# colum A = X[0] or 0 at x
# row 1 = Y[0] or  0 at y
# colum B at row number 2 = y[1],x[1]


# use for loop write colum A
for item in range(len(names)): # loop from 0 to 2 (index position)
   outSheet.write(item+1, 0, names[item])

# use for loop write colum B
for item in range(len(values)): # loop from 0 to 2 (index position)
   outSheet.write(item+1, 1, values[item])


'''
outSheet.write(1,1,names[0])
outSheet.write("A3",names[1])
outSheet.write("A4",names[2])

outSheet.write("B2",values[0])
outSheet.write("B3",values[1])
outSheet.write("B4",values[2])
'''


outWorkbook.close()