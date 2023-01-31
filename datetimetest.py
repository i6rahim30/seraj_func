from datetime import datetime
from datetime import timedelta
def check_found(appointment,appointments):
    for app in appointments:
        if app.date ==appointment.date and app.time ==  appointment.time:
            return False
    return True


def check_found(date,time,doctor,appointments):
    for app in appointments:
        if app.date ==date and app.time ==  time and app.doctor == doctor:
            return False
    return True

def get_date_object(datetime_str):
    return datetime.strptime(datetime_str, '%d/%m/%y')


def get_current_day(current_date,current_day):
    date=current_date+timedelta(days=1)
    while date.weekday() != current_day:
        date=date+timedelta(days=1)
    return  date

def get_doctor_next_day(current_date,sps):
    date=current_date+timedelta(days=0)
    do=True
    while do:
        date=date+timedelta(days=1)
        for sp in sps:
            if date.weekday()==int(sp.day) and sp.time!="11:00":
                do =False
                break
    print(sp.time)
    return date


def get_doctor_next_day2(current_date,doctor,appointments):
    date=current_date+timedelta(days=1)
    while check_avalible(doctor,date,appointments):
        date=date+timedelta(days=1)
    return date
    
def check_avalible(doctor,date,appointments):
    for sp in doctor.schedule.scedule_appintments:
        if date.weekday()==int(sp.day) and check_found(date,sp.time,doctor,appointments):
            print (sp.time)
            return False
    return True

        







datetime_str = '30/01/23'



datetime_object = datetime.strptime(datetime_str, '%d/%m/%y')




NextDay_Date = datetime.strptime(datetime_str, '%d/%m/%y') +timedelta(days=10)
#datetime.timedelta(days=2)
#print(NextDay_Date)
# print(type(datetime_object))
# print(datetime_object.NextDay_Date)  

#print(get_current_day(datetime_object,0))



