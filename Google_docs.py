import gspread
# Указываем путь к JSON
gc = gspread.service_account(filename='C:\\Users\\anton.kudryashov\\Downloads\\it-supprot-report-e01c2b540894.json')
#Открываем тестовую таблицу
sh = gc.open("MR Group IT support")
#Выводим значение ячейки A1
a = sh.sheet1.get('A713:C779')
for row in a:
    print(row)