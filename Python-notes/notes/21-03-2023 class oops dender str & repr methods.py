




class Dog:
    '''A python class to represent dog
     '''
    # Class attribute
    species = 'Canis familiaris'

    def __init__(self,name,age):
        '''param:
           name: str
           age: int
           Creates an instance of the dog class
           '''
        self.name = name
        self.age = age
# use describe method for description

# Use of __str__ dender str method

    def __str__(self):

        return f"{self.name} is {self.age} years old"
        
# Use of __repr__ method

    def __repr__(self):
        return f"{self.name} is {self.age} years old."
