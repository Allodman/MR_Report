import gspread
from datetime import datetime, date, time
# Указываем путь к JSON
gc = gspread.service_account(filename='C:\\Users\\anton.kudryashov\\Downloads\\it-supprot-report-e01c2b540894.json')
#Открываем тестовую таблицу
sh = gc.open("MR Group IT support")
ws = sh.worksheet("Обращения в поддержку")

#--------------------------------------
review_start_date = f"01.{datetime.timetuple(datetime.now())[1] - 1:02}.2022"
review_end_date = f"{30 if (ws.find())}"
print(review_start_date)
# q = cell = ws.find("31.06.2022")
# if q == None:
#     print("Good")

#--------------------------------------
#Выводим значение ячейки A1
# a = sh.sheet1.get('A800:C1000')
# for row in a:
#     print(row)
# print(a)
# a = '23/05/2022'
# b = datetime.strptime(a, '%d.%m.%Y').date()
