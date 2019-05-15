import time
import datetime
from datetime import date, timedelta

#1
def get_monday(date):
    pre = time.strptime(date + ' 1', '%Y %W %w')
    return time.asctime(pre)

print(get_monday('2015 50'))

#2
def get_all_sundays(year):

       first_date = date(year, 1, 1)
       first_sunday = first_date + timedelta(days = 6 - first_date.weekday())
       print(first_sunday)
       for n in range(51):
           first_sunday += timedelta(days = 7)
           print(first_sunday)

get_all_sundays(2019)

#3
def addYears(date_by_user, n):
    try:
        return date_by_user.replace(year = date_by_user.year + n)
    except ValueError:
        return date_by_user + (date(date_by_user.year + n, 1, 1) - date(date_by_user.year, 1, 1))

print(addYears(datetime.date(2015,1,1), -1))
print(addYears(datetime.date(2015,1,1), 0))
print(addYears(datetime.date(2015,1,1), 2))
print(addYears(datetime.date(2000,2,29),1))

#4
class PrintDateFormats():
    def print_all_date_formats(self):
        print("a: ", datetime.datetime.now())
        print("b: ", datetime.date.today().strftime("%Y"))
        print("c: ", datetime.date.today().strftime("%B"))
        print("d: ", datetime.date.today().strftime("%W"))
        print("e: ", datetime.date.today().strftime("%w"))
        print("f: ", datetime.date.today().strftime("%j"))
        print("g: ", datetime.date.today().strftime("%d"))
        print("h: ", datetime.date.today().strftime("%A"))

PrintDateFormats().print_all_date_formats()

#5
def convert_to_timestamp():
    return time.mktime(datetime.datetime.now().timetuple())

print(convert_to_timestamp())

#6
def convert_to_timestamp_two(date):
    return time.mktime(datetime.datetime.strptime(date, "%d-%m-%Y").timetuple())

print(convert_to_timestamp_two('01-01-2019'))

#7
def count_days_between_dates(date1, date2):
    first_date = datetime.datetime.strptime(date1, '%d-%m-%Y')
    second_date = datetime.datetime.strptime(date2, '%d-%m-%Y')
    return (second_date -  first_date).days

print(count_days_between_dates('01-01-2019', '01-02-2019'))


#8
def count_days_between_datetimes(date1, date2):
    return (date1 - date2).days

print(count_days_between_datetimes(datetime.datetime(2019,1,12,0,0,0), datetime.datetime(2019,12,10,0,0,0)))


#9
print(time.ctime())

#10
print(time.mktime(datetime.datetime.now().timetuple()))


#11
def count_seconds(date1, date2):
  return (date1 - date2).days * 24 * 3600 + (date1 - date2).seconds


print(count_seconds(datetime.datetime.strptime('2019-01-01 10:00:00', '%Y-%m-%d %H:%M:%S'), datetime.datetime.strptime('2019-01-01 11:00:00', '%Y-%m-%d %H:%M:%S')))


#12
def sub_five_days():
    return date.today() - timedelta(5)

print(sub_five_days())

#13
def convert_unix_str_to_date(unix_str):
    ts =  datetime.datetime.fromtimestamp(int(unix_str))
    return ts.strftime('%Y-%m-%d %H:%M:%S')

print(convert_unix_str_to_date('1557867328'))

#14
print('Yesterday: ', datetime.date.today() - datetime.timedelta(days = 1))
print('Today: ', datetime.date.today())
print('Tomorrow: ', datetime.date.today() + datetime.timedelta(days = 1))


#15
print(datetime.datetime.combine(date.today(), datetime.datetime.min.time()))


#16
print('1: ', datetime.date.today() + datetime.timedelta(days = 1))
print('2: ', datetime.date.today() + datetime.timedelta(days = 2))
print('3: ', datetime.date.today() + datetime.timedelta(days = 3))
print('4: ', datetime.date.today() + datetime.timedelta(days = 4))
print('5: ', datetime.date.today() + datetime.timedelta(days = 5))



#17

def if_leap_year(year):
    if year % 100 == 0:
        return False
    elif year % 400 ==0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

print(if_leap_year(2018))
print(if_leap_year(2008))

#18
def convert_str_to_datetime(date_str):
    return datetime.datetime.strptime(date_str, '%b %d %Y %I:%M%p')


print(convert_str_to_datetime("Jan 1 2014 2:43PM"))

#19
print(datetime.datetime.now().time())

#20
def add_5second():
    print(datetime.datetime.now())
    print(datetime.datetime.now() + datetime.timedelta(0,5))

add_5second()
