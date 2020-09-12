from xlwt import Workbook


wb = Workbook()

ws = wb.add_sheet('teacher')

ws.write(0, 0, 'Username')
ws.write(0, 1, 'Password')
ws.write(0, 2, 'Email')

ws.write(1, 0, 'Rajam')
ws.write(1, 1, 'Something123')
ws.write(1, 2, 'rajamucsmdy@gmail.com')

ws.write(2, 0, 'Pooja')
ws.write(2, 1, 'getme8382')
ws.write(2, 2, 'pdl38987@gmail.com')

ws.write(3, 0, 'Clikot')
ws.write(3, 1, 'saveme8298')
ws.write(3, 2, 'cikot87363@cyberper.net')

ws.write(4, 0, 'Unknown')
ws.write(4, 1, 'ieiei1882')
ws.write(4, 2, 'erdverwehung@redviet.com')

wb.save('email_list.xls')

print('Sheet is successfully created.')

