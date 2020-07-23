class Car:
    
    sound="Beep Beep"
    
    def __init__(self,color=None,max_speed=None,acceleration=None,tyre_friction=None):
        self._color=color
        if max_speed >= 0:
            self._max_speed=max_speed
        else:
            raise ValueError("Invalid value for max_speed")
        if acceleration >= 0:    
            self._acceleration=acceleration
        else:
            raise ValueError("Invalid value for acceleration")
        if tyre_friction >= 0:
            self._tyre_friction=tyre_friction
        else:
            raise ValueError("Invalid value for tyre_friction")
        
        self._current_speed=0
        self._is_engine_started=False
    """@staticmethod
    def check_value(value,variable):
        if value > 0:
            self._value=
        else:
            raise ValueError("Invalid value for {}".format(variable))"""
        
    def start_engine(self):
        self._is_engine_started=True
        
    def stop_engine(self):
        self._is_engine_started=False
        
    def accelerate(self):
        if self._is_engine_started:
            speed=self._current_speed + self._acceleration
            if speed < self._max_speed:
                self._current_speed+=self._acceleration
            else: 
                self._current_speed=self._max_speed
            
        else:
            print("Start the engine to accelerate")
        
    def apply_brakes(self):
        self._current_speed-=self._tyre_friction
        if self._current_speed <= 0:
            self._current_speed=0
    
    def sound_horn(self):
        if self._is_engine_started:
            self.sound_horn_voice()
        else:
            print("Start the engine to sound_horn")
    
    @classmethod
    def sound_horn_voice(cls):
        print(cls.sound)
        
    @property
    def color(self):
        return self._color
        
    @property
    def max_speed(self):
        return self._max_speed
            
    @property
    def acceleration(self):
        return self._acceleration
            
    @property
    def tyre_friction(self):
        return self._tyre_friction
        
    @property
    def current_speed(self):
        return self._current_speed
        
    @property
    def is_engine_started(self):
        return self._is_engine_started
            
class Truck(Car):
    
    sound="Honk Honk"
    
    def __init__(self,color,max_speed,acceleration,tyre_friction,max_cargo_weight=None):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        self._max_cargo_weight=max_cargo_weight
        self._current_speed=0
        self._is_engine_started=False
        self.load_value=0
        
    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight
        
    def load(self,value):
        if self._current_speed:
            print("Cannot load cargo during motion")
        else:
            if value < 0:
                raise ValueError("Invalid value for cargo_weight")
            elif self.load_value + value > self._max_cargo_weight:
                print("Cannot load cargo more than max limit: {}".format(self._max_cargo_weight))
            else:
                temp=self.load_value + value
                if temp <= self._max_cargo_weight:
                    self.load_value=temp
                else:
                    self.load_value=self._max_cargo_weight
                
                
    
    def unload(self,value):
        if self._current_speed:
            print("Cannot unload cargo during motion")
        else:
            if value < 0:
                raise ValueError("Invalid value for cargo_weight")
            elif value > self.load_value:
                print("Cannot unload cargo more than max limit: {}".format(self._max_cargo_weight))
            else:
                self.load_value -= value
                if self.load_value < 0:
                    self.load_value=0
        
        
class RaceCar(Car):
    
    sound="Peep Peep\nBeep Beep"
    
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        self._current_speed=0
        self._is_engine_started=False
        self._nitro=0
        
    @property
    def nitro(self):
        return self._nitro
        
    def accelerate(self):
        import math
        value=0
        if self._is_engine_started:
            if self._nitro > 0:
                value=(30/100)*self._acceleration
                self._nitro-=10
            speed=math.ceil((self._current_speed + value + self._acceleration))
            if speed <= self._max_speed:
                self._current_speed=speed
            else:
                self._current_speed=self._max_speed
        else:
            print("Start the engine to accelerate")
    
    def apply_brakes(self):
        if self._current_speed > self._max_speed/2:
            self._nitro+=10
        self._current_speed-=self._tyre_friction
        if self._current_speed < 0:
            self._current_speed=0

    