import datetime

now_data = [int(input("请输日期:"))for i in range(3)]
data_tuple = tuple(now_data)
startdata = (data_tuple[0],1,1)
def days_before_date(year, month, day):
    time_diff = datetime.date(year, month, day) - datetime.date(*startdata)
    return time_diff.days
print(days_before_date(*data_tuple))