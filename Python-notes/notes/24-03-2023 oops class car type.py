'''Create a car class.
2 Instance attributes
i) color
ii) horse_power
'''

class Car():


    def __init__(self,color,horse_power,maker,odo,car_type,\
                 transmission = 'Manual'):
        self.color = color
        self.horse_power = horse_power
        self.maker = maker
        self.odo = odo
        self.car_type = car_type
        if transmission.lower() not in ('Manual','Auto'):
            raise ValueError('Transmission has to be either manual or auto only.')
        
        self.transmission = transmission


    def drive():
        pass
        
