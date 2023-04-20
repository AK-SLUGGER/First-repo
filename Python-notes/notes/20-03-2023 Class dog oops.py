




class Dog:
    # Class attribute
    species = 'Canis familiaris'

    def __init__(self,name,age):
        self.name = name
        self.age = age
# use describe method for description

    
    def describe(self):
        return (f'{self.name} is {self.age} years old')
    
