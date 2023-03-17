


class Student():

    def __init__(self,name,roll):
        self.name = name
        self.roll=roll
        

    def set_previous_school(self,school_name = None):
        self.previous_school= school_name

    def get_previous_school(self):
        try:
            if self.previous_school == None:
                return "Please set the previous school before fetching it"

        except AttributeError:
            return"First please call the set_previous_school method"
            
        return self.previous_school

    def update_roll(self,roll):
        self.roll=roll

    def get_roll(self):
        return self.roll
