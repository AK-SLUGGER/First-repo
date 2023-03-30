

#28-03-2023

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
        

    def gear_shift(self,speed):
        self.speed=speed
        self.gear=None
        if self.speed in range(0,30):
            self.gear=1
        elif self.speed in range(30,50):
            self.gear=2
        elif self.speed in range(50,71):
            self.gear=3
        elif self.speed in range(80,120):
            self.gear=4
        else:
            return "Overspeeding"

        return self.gear

