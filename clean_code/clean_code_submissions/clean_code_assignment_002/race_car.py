import math
from car import Car


class RaceCar(Car):
    vehicle_sound = "Peep Peep\nBeep Beep"

    def __init__(self, color, max_speed, acceleration, tyre_friction):
        super().__init__(color, max_speed, acceleration, tyre_friction)
        self._current_speed = 0
        self._is_engine_started = False
        self._nitro = 0

    @property
    def nitro(self):
        return self._nitro

    def accelerate(self):
        super().accelerate()
        temp = 0
        if self._nitro > 0:
            temp = (0.3)*self._acceleration
            self._nitro -= 10
            self._current_speed = math.ceil((self._current_speed + temp))
            if self._current_speed > self._max_speed:
                self._current_speed = self._max_speed

    def apply_brakes(self):
        if self._current_speed > (self._max_speed / 2):
            self._nitro += 10
        super().apply_brakes()
