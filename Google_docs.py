import gspread
import re
from datetime import datetime, date, time
# Указываем путь к JSON
gc = gspread.service_account(filename='C:\\Users\\anton.kudryashov\\Downloads\\it-supprot-report-e01c2b540894.json')
# Открываем тестовую таблицу
sh = gc.open("MR Group IT support")
ws = sh.worksheet("Обращения в поддержку")

# Область поиска необходимых дат начала и конца отчёта
search_range = ws.get("A500:C5000")

# Поиск даты начала отчёта
for row in search_range:
    b = re.search(r'\d\d' + '.' + f'{datetime.timetuple(datetime.now())[1]-1:02}.{datetime.timetuple(datetime.now())[0]}', row[0])
    if b != None:
        review_start_date = str(b)[39:49] # Дата начала отчёта
        break

# Поиск ячейки начала отчёта по дате
cell_review_start_date = f'{str(ws.find(review_start_date))[6:12]}'

# Поиск даты конца отчёта (Технически это первый день отчёта текущего месяца
for row in search_range:
    c = re.search(r'\d\d' + '.' + f'{datetime.timetuple(datetime.now())[1]:02}.{datetime.timetuple(datetime.now())[0]}', row[0])
    if c != None:
        review_end_date = str(c)[39:49]
        print(review_end_date)
        break

# Поиск ячейки конца отчёта по дате
cell_review_end_date_incorrect = f'{str(ws.find(review_end_date))[6:12]}'

# Путём тупых манипуляци изменяем ячейку первого дня текущего месяца на ячейку последнего дня предыдущего месяца
correct_num = int(cell_review_end_date_incorrect[3]) - 1
cell_review_end_date = str(cell_review_end_date_incorrect[:3] + str(correct_num) + cell_review_end_date_incorrect[4] + '3')

# Проверка правильности парсинга
last_month_review = ws.get(f'{cell_review_start_date}:{cell_review_end_date}')
for row in last_month_review:
    print(row)