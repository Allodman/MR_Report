import gspread
import re
from datetime import datetime, date, time
# Указываем путь к JSON
gc = gspread.service_account(filename='C:\\Users\\anton.kudryashov\\Downloads\\it-supprot-report-e01c2b540894.json')
# Открываем тестовую таблицу
sh = gc.open("MR Group IT support")
ws = sh.worksheet("Обращения в поддержку")

#--------------------------------------

# Вариант подходит только  если на 30 и 31 не выпадают выходные
# review_start_date = f"01.{datetime.timetuple(datetime.now())[1] - 1:02}.2022"
# review_end_date = f"{f'30.{datetime.timetuple(datetime.now())[1] - 1:02}.2022' if (ws.find(f'31.{datetime.timetuple(datetime.now())[1] - 1:02}.2022')) == None else f'31.{datetime.timetuple(datetime.now())[1] - 1:02}.2022' }"
# print(review_start_date)
# print(review_end_date)
# print(ws.find('30.07.2022'))
#
# cell_review_start_date = f'{str(ws.find(review_start_date))[6:12]}'
# cell_review_end_date = f'{str(ws.find(review_end_date))[6:11]}3'
# print(str(cell_review_start_date))
# print(str(cell_review_end_date))

# Через регулярные выражение
# print(r'\d\d' + f'{datetime.timetuple(datetime.now())[1]-1:02}.{datetime.timetuple(datetime.now())[0]}')
# d = r'\d\d' + f'{datetime.timetuple(datetime.now())[1]-1:02}.{datetime.timetuple(datetime.now())[0]}'



#--------------------------------------
# a = sh.sheet1.get(f'{cell_review_start_date}:{cell_review_end_date}')
search_range = ws.get("A500:C5000")
for row in search_range:
    b = re.search(r'\d\d' + '.' + f'{datetime.timetuple(datetime.now())[1]-1:02}.{datetime.timetuple(datetime.now())[0]}', row[0])
    if b != None:
        review_start_date = str(b)[39:49] # Дата начала отчёта
        break
cell_review_start_date = f'{str(ws.find(review_start_date))[6:12]}' # Ячейка начала отчёта

for row in search_range:
    b = re.findall(r'\d\d' + '.' + f'{datetime.timetuple(datetime.now())[1]:02}.{datetime.timetuple(datetime.now())[0]}',row[0])
    print(b)


# print(review_start_date)
# print(cell_review_start_date)
# a = '23/05/2022'
# b = datetime.strptime(a, '%d.%m.%Y').date()
