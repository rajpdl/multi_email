from xlrd import open_workbook


wb = open_workbook('email_list.xls')

ws = wb.sheet_by_index(0)

receList = []

for i in range(ws.nrows):
    for j in range(ws.ncols):
        if ws.cell_value(i, j) == 'Email':
            print(ws.cell_value(0, j))
            print(i, j)
            i = 1
            while i < ws.nrows:
                print(ws.cell_value(i, j))
                receList.append(ws.cell_value(i, j))
                i += 1
        # print(ws.cell_value(i, j))

print(receList)
    