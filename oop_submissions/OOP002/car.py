class Car:
    
    sound="Beep Beep"
    
    def __init__(self,color=None,max_speed=None, acceleration=None, tyre_friction=None):
        self._color=color
        
        if max_speed >= 0:
            self._max_speed=max_speed
        else:
            raise ValueError("Invalid value for max_speed")
        
        if acceleration >=0:
            self._acceleration=acceleration
        else:
            raise ValueError("Invalid value for acceleration")
        
        if tyre_friction >=0:
            self._tyre_friction=tyre_friction
        else:
            raise ValueError("Invalid value for tyre_friction")
        
        self._is_engine_started=False
        self._current_speed=0
     
    def start_engine(self):
         self._is_engine_started=True
    
    def accelerate(self):
        if self._is_engine_started:
            if self._current_speed < self._max_speed:
                value=self._current_speed + self._acceleration
                if value < self._max_speed:
                    self._current_speed+=self._acceleration
                else: 
                    self._current_speed=self._max_speed
        else:
            print("Start the engine to accelerate")
    
    
    def apply_brakes(self):
        self._current_speed-=self._tyre_friction
        if self._current_speed < 0:
            self._current_speed=0
            
    def sound_horn(self):
        if self._is_engine_started:
            self.sound_horn2()
        else:
            print("Start the engine to sound_horn")
    
    @classmethod
    def sound_horn2(cls):
        print(cls.sound)
    
    def stop_engine(self):
        self._is_engine_started=False
        
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
         
    @property
    def is_engine_started(self):
         return self._is_engine_started
            
        
        
class Truck(Car):
    
    sound="Honk Honk"
    
    def __init__(self,color,max_speed,acceleration,tyre_friction,max_cargo_weight):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        self.max_cargo_weight=max_cargo_weight
        self._is_engine_started=False
        self._current_speed=0
        self.loading=0
        
    def load(self,value):
        if self._current_speed:
            print("Cannot load cargo during motion")
        else:
            if value >=0:
                a=self.loading + value
                if a <= self.max_cargo_weight:
                    self.loading+=value
                else:
                    print("Cannot load cargo more than max limit: ",self.max_cargo_weight)
            else:
                raise ValueError("Invalid value for cargo_weight")
                
    def unload(self,value):
        if self._current_speed:
            print("Cannot unload cargo during motion")
        else:
            if value >=0:
                if value <= self.loading:
                    self.loading-=value
                else:
                    print("Cannot unload cargo more than max limit: ",self.loading)
            else:
                raise ValueError("Invalid value for cargo_weight")
                
class RaceCar(Car):
    
    sound="Peep Peep\nBeep Beep"
    
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        self._is_engine_started=False
        self._current_speed=0
        self._nitro=0
        
    @property
    def nitro(self):
         return self._nitro
        
    def accelerate(self):
        if self._is_engine_started:
            if (self._nitro > 0) and (self._current_speed < self._max_speed):
                a=(30/100)*self._acceleration
                b=self._current_speed+int(a)
                if b < self._max_speed:
                    self._current_speed+=int(a)+self._acceleration
                else:
                    self._current_speed=self._max_speed
                self._nitro-=10
            else:
                a=self._current_speed + self._acceleration
                if a < self._max_speed:
                    self._current_speed+=self._acceleration
                else:
                    self._current_speed=self._max_speed
                
        else:
            print("Start the engine to accelerate")
    
    def apply_brakes(self):
        if self._is_engine_started:
            if self._current_speed > self._max_speed/2:
                self._nitro+=10
            if self._current_speed > self._tyre_friction:
                self._current_speed-=self._tyre_friction
 