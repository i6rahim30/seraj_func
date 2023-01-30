from datetime import datetime
from datetime import timedelta


def get_current_day(current_date,current_day,current_time=None):
    date=current_date+timedelta(days=1)
    while date.weekday() != current_day:
        date=date+timedelta(days=1)
    return  date

def get_doctor_next_day(current_date,sps):
    date=current_date+timedelta(days=1)
    print("!!!!!!11")
    for sp in sps:
        sp_ob=get_date_object(sp.date)
        print(sp_ob,"----",date)
        if sp.date==date:
            return date
        


def get_date_object(datetime_str):
    return datetime.strptime(datetime_str, '%d/%m/%y')




datetime_str = '30/01/23'



datetime_object = datetime.strptime(datetime_str, '%d/%m/%y')




NextDay_Date = datetime.strptime(datetime_str, '%d/%m/%y') +timedelta(days=10)
#datetime.timedelta(days=2)
#print(NextDay_Date)
# print(type(datetime_object))
# print(datetime_object.NextDay_Date)  

print(get_current_day(datetime_object,0))



