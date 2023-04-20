'''Create a car class.
2 Instance attributes
i) color
ii) horse_power
'''

class Car():


    def __init__(self,color,horse_power,maker,odo,car_type,\
                 transmission = 'manual'):
        self.color = color
        self.horse_power = horse_power
        self.maker = maker
        self.odo = odo
        self.car_type = car_type
        if transmission.lower() not in ('manual','auto'):
            raise ValueError('Transmission has to be either manual or auto only.')
        
        self.transmission = transmission

    def drive(self,distance):
        '''param:
             distance an int that represents the distance to be covered

             returns:
             updated odometer value

             '''
        self.odo += distance
        return self.odo
             

