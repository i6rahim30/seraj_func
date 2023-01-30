from doctor import Doctor
from patient import Patient
from apppointment import Appointment
from schedule import Schedule
from scedule_appintment import Scedule_Appintment
import datetimetest



def check_found(appointment):
    for app in appointments:
        if app.date ==appointment.date and app.time ==  appointment.time:
            return False
    return True

def show_schedule(schedule):
    for sp in schedual.scedule_appintments:
        print(sp.date,"-",sp.time,"\n")
    

def add_ppointment(new_app):
    if check_found(new_app):
        appointments.append(new_app)
        print ("Added In Date :",new_app.date," In Time : ",new_app.time," With Doctor",new_app.doctor)
    else:
        print ("Found In Time : ",new_app.date,"In Time : ",new_app.time," With Doctor",new_app.doctor)
"""
def reschedule(ap):
    date=datetimetest.get_date_object(ap.date)
    last_date=datetimetest.get_current_day(date,date.weekday())
    ap.date=last_date
    print ("Added In Date :",ap.date," In Time : ",ap.time," With Doctor",ap.doctor)
"""

def reschedule(ap):
    date=datetimetest.get_date_object(ap.date)

    last_date=datetimetest.get_doctor_next_day(date,ap.doctor.schedule.scedule_appintments)

    ap.date=last_date
    print ("Added In Date :",ap.date," In Time : ",ap.time," With Doctor",ap.doctor)

sps=[]
appointments=[]



sp1=Scedule_Appintment('30/01/23',"9:00")
sps.append(sp1)
sp2=Scedule_Appintment('30/01/23',"11:00")
sps.append(sp2)
sp3=Scedule_Appintment('01/02/23',"11:00")
sps.append(sp3)

schedual=Schedule(sps)

doc1=Doctor("mohamed","Bones",schedual)
show_schedule(doc1.schedule)
patient1=Patient("Ahmed",25)

ap=Appointment(doc1,patient1,sp1.date,sp1.time)
add_ppointment(ap)
ap2=Appointment(doc1,patient1,sp2.date,sp2.time)
add_ppointment(ap2)
ap3=Appointment(doc1,patient1,sp2.date,"9:00")
add_ppointment(ap3)

reschedule(ap2)





print("--------------------")

