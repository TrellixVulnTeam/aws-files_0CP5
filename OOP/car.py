
class Car:
    
    sound="Beep Beep"
    
    def __init__(self,color=None,max_speed=None, acceleration=None, tyre_friction=None):
        self._color=color
        
        if max_speed >= 0:
            self._max_speed=max_speed
        else:
            raise ValueError("Invalid value for max_speed")
        self._acceleration=acceleration
        self._tyre_friction=tyre_friction
        self.is_engine_started=False
        self._current_speed=0
     
    def start_engine(self):
         self.is_engine_started=True
    
    def accelerate(self):
        if self.is_engine_started:
            if self._current_speed < self._max_speed:
                self._current_speed+=self._acceleration
        else:
            print("Start the engine to accelerate")
    
    
    def apply_brakes(self):
        self._current_speed-=self._tyre_friction
    
    def sound_horn(self):
        if self.is_engine_started:
            self.sound_horn2()
        else:
            print("Start the engine to sound_horn")
    
    @classmethod
    def sound_horn2(cls):
        print(cls.sound)
    
    def stop_engine(self):
        self.is_engine_started=False
        
    @property
    def current_speed(self):
         return self._current_speed
         
    @property
    def max_speed(self):
         return self._max_speed
         
    @property
    def color(self):
         return self._color
    @property
    def acceleration(self):
         return self._acceleration
         
    @property
    def tyre_friction(self):
         return self._tyre_friction
            
   # def set_current_speed(self,current_speed):
    #    self._current_speed=current_speed
        
        
class Truck(Car):
    
    sound="Honk Honk"
    
    def __init__(self,color,max_speed,acceleration,tyre_friction,max_cargo_weight):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        self.max_cargo_weight=max_cargo_weight
        self.is_engine_started=False
        self._current_speed=0
        
    def load(self,value):
        if self._current_speed:
            print("Cannot load cargo during motion")
        else:
            if value >=0:
                if self.max_cargo_weight > value:
                    self.max_cargo_weight
                else:
                    print("Cannot load cargo more than max limit: 100")
            else:
                raise ValueError("Invalid value for cargo_weight")
                
        
    
                
            
            
            
class RaceCar(Car):
    
    sound="Peep Peep\nBeep Beep"
    
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        self.is_engine_started=False
        self._current_speed=0
        self.nitro=0
        
    def accelerate(self):
        if self.is_engine_started:
            if (self.nitro > 0) and (self._current_speed < self._max_speed):
                a=(30/100)*self._acceleration
                b=self._current_speed+int(a)
                if b < self._max_speed:
                    self._current_speed+=int(a)+self._acceleration
                    self.nitro-=10
            else:
                self._current_speed+=self._acceleration
                
        else:
            print("Start the engine to accelerate")
    
    def apply_brakes(self):
        if self._current_speed > self._max_speed/2:
            self.nitro+=10
        self._current_speed-=self._tyre_friction
        
    
        
        
        
"""
from car import Car  
>>> car = Car(color="Red", max_speed=250, acceleration=10, tyre_friction=3)  
>>> car.acceleration  
10  
>>> car.tyre_friction  
3  
>>> car.max_speed  
250  
>>> car.color  
Red  

>>> from car import Car  
>>> car = Car(color="Red", max_speed=-250, acceleration=10, tyre_friction=3)  
ValueError: Invalid value for max_speed  


from car import Car  
>>> car = Car(max_speed=250, acceleration=10, tyre_friction=3)  
>>> car.start_engine()  
>>> car.is_engine_stared
True

from car import Car  
>>> car = Car(max_speed=250, acceleration=10, tyre_friction=3)  
>>> car.current_speed  
0  

> car = Car(max_speed=250, acceleration=10, tyre_friction=3)  
>>> car.start_engine()  
>>> car.accelerate()  
>>> car.current_speed  
10  
>>> car.accelerate()  
>>> car.current_speed  
20
...
...
...
>>> car.current_speed
250
>>> car.accelerate()  
>>> car.current_speed
250

>>> car = Car(max_speed=250, acceleration=10, tyre_friction=3)  
>>> car.accelerate()  
Start the engine to accelerate  

car = Car(max_speed=250, acceleration=10, tyre_friction=3)  
>>> car.start_engine()  
>>> car.accelerate()  
>>> car.current_sped  
10  
>>> car.apply_brakes()  
>>> car.current_sped  
7  


car = Car(max_speed=250, acceleration=10, tyre_friction=3)  
>>> car.start_engine()  
>>> car.sound_horn()  
"Beep Beep"  
>>> car = Car(max_speed=250, acceleration=10, tyre_friction=3)  
>>> car.sound_horn()  
Start the engine to sound_horn  

car = Car(max_speed=250, acceleration=10, tyre_friction=3)  
>>> car.start_engine()  
>>> car.is_engine_stared
True
>>> car.stop_engine()  
>>> car.is_engine_stared
False




car = Car(max_speed=250, acceleration=10, tyre_friction=3)  
>>> car.current_speed  # call to getter method
0  
>>> car.start()  
>>> car.current_speed  # call to getter method
10  
>>> car.current_speed = 10  
AttributeError: can't set attribute


>>> truck = Truck(color="Red", max_speed=250, acceleration=10, tyre_friction=3, max_cargo_weight=100)  
>>> truck.load(50)  
>>> truck.load(100)  
Cannot load cargo more than max limit: 100  
>>> truck.load(-100)  
ValueError: Invalid value for cargo_weight
>>> truck = Truck(color="Red", max_speed=250, acceleration=10, tyre_friction=3, max_cargo_weight=100)  
>>> truck.start_engine()  
>>> truck.accelerate()  
>>> truck.load(50)  
Cannot load cargo during motion 
>>> truck.sound_horn()  
Honk Honk  


Now we need a RaceCar in our cars world.
A RaceCar is a Car but with the following additional behaviours

horn sounds like “Peep Peep\nBeep Beep”
On applying brakes at more than half the max speed it get 10 nitro.
10 nitro points is fixed for all the RaceCars.
When car accelerates when nitro is available it gets additional 30% of acceleration value (rounded to int - ceil) as speed within max limits. And nitro get reduced by 10 points
Should be able to see nitro
Coding Guidelines:

You can use the same car class built in the Part 1 of this assigment
Continue writing code in the same car.py file
>>> racecar = RaceCar(color="Red", max_speed=250, acceleration=50, tyre_friction=30)  
>>> racecar.start_engine()  
>>> racecar.accelerate()  
>>> racecar.accelerate()  
>>> racecar.accelerate()  
>>> racecar.current_speed  
150  
>>> racecar.apply_brakes()  
>>> racecar.current_speed  
120  
>>> racecar.nitro  
10  
>>> racecar.accelerate()  
>>> racecar.current_speed  
185 # 120 + 50 + (50 * 30 / 100)  
>>> racecar.nitro  
0  
>>> car.sound_horn()  
Peep Peep
Beep Beep





"""