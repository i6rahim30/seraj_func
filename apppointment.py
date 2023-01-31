import datetimetest
class Appointment :
    def __init__(self,doctor,patient,date,time,appointments=None):
       self.doctor=doctor
       self.patient =patient
       if isinstance(date, str):
            self.date=datetimetest.get_date_object(date)
       else:
            self.date=date

       self.time=time
       self.appointments=appointments

    
    


