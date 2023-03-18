






class student():

    def __init__(self,name,roll_no):# double __ called dunder methods
        self.name=name
        self.roll_no = roll_no
        

    def set_previous_school(self,school_name):
        self.previous_school = input ('Previous School:')
        
    def get_previous_school(self):
        return self.previous_school
