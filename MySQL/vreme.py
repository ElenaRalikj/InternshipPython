from datetime import datetime

date_time_str = '21/09/19 01:55:19'

date_time_obj = datetime.strptime(date_time_str, '%y/%m/%d %H:%M:%S')

print(type(date_time_obj))
print(date_time_obj)