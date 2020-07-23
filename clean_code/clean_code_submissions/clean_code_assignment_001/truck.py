from car import Car


class Truck(Car):
    vehicle_sound = "Honk Honk"

    def __init__(self, color, max_speed, acceleration,
                 tyre_friction, max_cargo_weight):
        if max_cargo_weight > 0:
            self._max_cargo_weight = max_cargo_weight
        else:
            raise ValueError("Invalid value for max_cargo_weight")
        super().__init__(color, max_speed, acceleration, tyre_friction)
        self._current_speed = 0
        self._is_engine_started = False
        self.current_load_weight = 0

    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight

    def load(self, load_value):
        if self._current_speed:
            print("Cannot load cargo during motion")
        else:
            if load_value < 0:
                raise ValueError("Invalid value for cargo_weight")
            temp = self.current_load_weight + load_value
            if temp <= self._max_cargo_weight:
                self.current_load_weight = temp
            else:
                print("Cannot load cargo more than max limit: {}"
                      .format(self._max_cargo_weight))

    def unload(self, unload_value):
        if self._current_speed:
            print("Cannot unload cargo during motion")
        else:
            if unload_value < 0:
                raise ValueError("Invalid value for cargo_weight")
            if unload_value <= self.current_load_weight:
                self.current_load_weight -= unload_value
