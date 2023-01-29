class Appointment :
    def __init__(self,doctor,patient,day):
        for d in doctor.schedule.day :
            for t in doctor.schedule.time :
                
            if d == day :
                return
            else :
                exit
        
        print("doctor Not Available")