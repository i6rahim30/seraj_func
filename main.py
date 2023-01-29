from doctor import Doctor
from patient import Patient
from apppointment import Appointment


doc_1=Doctor("Dr.Ahmed","cardiology")
pat_1=Patient("Ali",25)

day = input("Please Enter The Day : ")
app_1=Appointment(doc_1,pat_1,{})


