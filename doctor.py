from schedule import Schedule

class Doctor :
    name=''
    department=''
    schedule=None
    def __init__(self,name,department,schedule) :
        self.name=name
        self.department=department
        self.schedule=schedule