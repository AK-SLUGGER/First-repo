


class Student():

    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no

    def set_previous_school(self,school_name=None):
        self.previous_school =school_name

    def get_previous_school(self):
        try:
            if self.previous_school == None:
                return "Please set the previous school before fetching"
        except AttributeError:
            return "First please call the set_previous_school method"
        return self.previous_school


    def update_roll_no(self,roll_no):
        self.roll_no = roll_no

    def get_roll_no(self):
        return self.roll_no
    
 
