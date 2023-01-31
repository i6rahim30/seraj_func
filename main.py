from doctor import Doctor
from patient import Patient
from apppointment import Appointment
from schedule import Schedule
from scedule_appintment import Scedule_Appintment
import datetimetest


def show_schedule(schedule):
    for sp in schedual.scedule_appintments:
        print(sp.day,"-",sp.time,"\n")

def show_apppointment(apps):
    for app in apps:
        print(app.doctor.name,"-",app.patient.name,"-",app.date,"-",app.time,"\n")
    

def add_ppointment(new_app):
    #if datetimetest.check_found(new_app.date,new_app.time,new_app.doctor,appointments):
    appointments.append(new_app)
"""
def reschedule(ap):
    date=datetimetest.get_date_object(ap.date)
    last_date=datetimetest.get_current_day(date,date.weekday())
    ap.date=last_date
    print ("Added In Date :",ap.date," In Time : ",ap.time," With Doctor",ap.doctor)
"""

def reschedule(ap):  # return avavlible Time 
    last_date=datetimetest.get_doctor_next_day2(ap.date,ap.doctor,appointments)
    print ("Added In Date :",last_date," In Time : ",ap.time," With Doctor",ap.doctor)

sps=[]
appointments=[]



sp1=Scedule_Appintment('0',"12:00")
sps.append(sp1)
sp2=Scedule_Appintment('1',"11:00")
sps.append(sp2)
sp3=Scedule_Appintment('2',"11:00")
sps.append(sp3)
sp4=Scedule_Appintment('5',"12:00")
sps.append(sp4)
schedual=Schedule(sps)

doc1=Doctor("mohamed","Bones",schedual)
#show_schedule(doc1.schedule)
patient1=Patient("Ahmed",25)

ap=Appointment(doc1,patient1,"31/01/23","11:00")
add_ppointment(ap)
ap2=Appointment(doc1,patient1,"31/01/23","11:00")
add_ppointment(ap2)
ap3=Appointment(doc1,patient1,"01/02/23","11:00")
add_ppointment(ap3)


show_apppointment(appointments)
reschedule(ap2)
#01/02/23


print("--------------------")

