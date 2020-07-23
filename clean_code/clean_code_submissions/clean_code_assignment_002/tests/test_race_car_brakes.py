from race_car import RaceCar


# case-15
def test_apply_brakes_to_race_car_and_update_current_speed():

    # Arrange
    race_car = RaceCar(
        color='DarkSeaGreen',
        max_speed=100,
        acceleration=10,
        tyre_friction=10
    )
    current_speed_value = 0
    race_car.start_engine()
    race_car.accelerate()

    # Act
    race_car.apply_brakes()

    # Assert
    assert race_car.current_speed == current_speed_value


# case-15
def test_apply_brakes_to_race_car_when_current_speed_more_than_half_the_max_speed_and_update_nitro():

    # Arrange
    race_car = RaceCar(
        color='DarkSlateBlue',
        max_speed=100,
        acceleration=20,
        tyre_friction=10
    )
    race_car.start_engine()
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()
    nitro_value = 10

    # Act
    race_car.apply_brakes()

    # Assert
    assert race_car.nitro == nitro_value


def test_apply_brakes_to_race_car_when_current_speed_is_equal_to_half_the_max_speed_and_nitro_value():

    # Arrange
    race_car = RaceCar(
        color='DarkSlateGrey',
        max_speed=100,
        acceleration=25,
        tyre_friction=10
    )
    race_car.start_engine()
    race_car.accelerate()
    race_car.accelerate()
    nitro_value = 0

    # Act
    race_car.apply_brakes()

    # Assert
    assert race_car.nitro == nitro_value


def test_apply_brakes_to_race_car_when_current_speed_not_more_than_half_the_max_speed_and_nitro_value():

    # Arrange
    race_car = RaceCar(
        color='DarkViolet',
        max_speed=100,
        acceleration=20,
        tyre_friction=10
    )
    race_car.start_engine()
    race_car.accelerate()
    race_car.accelerate()
    nitro_value = 0

    # Act
    race_car.apply_brakes()

    # Assert
    assert race_car.nitro == nitro_value


# case-16
def test_apply_brakes_when_race_car_current_speed_is_less_than_tyre_friction():

    # Arrange
    race_car = RaceCar(
        color='DeepPink',
        max_speed=20,
        acceleration=9,
        tyre_friction=10
    )
    current_speed_value = 0
    race_car.start_engine()
    race_car.accelerate()

    # Act
    race_car.apply_brakes()

    # Assert
    assert race_car.current_speed == current_speed_value


# case-17
def test_apply_brakes_when_race_car_current_speed_is_more_than_tyre_friction():

    # Arrange
    race_car = RaceCar(
        color='DeepSkyBlue',
        max_speed=4,
        acceleration=4,
        tyre_friction=3
    )
    current_speed_value = 1
    race_car.start_engine()
    race_car.accelerate()

    # Act
    race_car.apply_brakes()

    # Assert
    assert race_car.current_speed == current_speed_value
