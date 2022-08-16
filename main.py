import calendar
from datetime import datetime, date, time


current_year = datetime.timetuple(datetime.now())[0]
current_month = datetime.timetuple(datetime.now())[1]
corrent_day = datetime.timetuple(datetime.now())[2]

print((calendar.monthrange(datetime.timetuple(datetime.now())[0], datetime.timetuple(datetime.now())[1] - 1))[1])