from race_car import RaceCar


# case-11
def test_accelerate_race_car_when_no_nitro_and_update_current_speed():

    # Arrange
    race_car = RaceCar(
        color='DarkMagenta',
        max_speed=20,
        acceleration=10,
        tyre_friction=5
    )
    current_speed_value = 10
    race_car.start_engine()

    # Act
    race_car.accelerate()

    # Assert
    assert race_car.current_speed == current_speed_value


# case-11
def test_accelerate_race_car_when_nitro_available_and_update_current_speed():

    # Arrange
    color = 'DarkOliveGreen'
    max_speed = 20
    acceleration = 6
    tyre_friction = 3
    race_car = RaceCar(
        color=color,
        max_speed=max_speed,
        acceleration=acceleration,
        tyre_friction=tyre_friction
    )
    current_speed_value = 17
    race_car.start_engine()
    race_car.accelerate()
    race_car.accelerate()
    race_car.apply_brakes()

    # Act
    race_car.accelerate()

    # Assert
    assert race_car.current_speed == current_speed_value


# case-12
def test_accelerate_race_car_when_engine_stoped_and_print_start_engine(
        capfd):

    # Arrange
    race_car = RaceCar(
        color='DarkOrange',
        max_speed=20,
        acceleration=10,
        tyre_friction=5
    )
    start_engine_to_accelerate = "Start the engine to accelerate\n"

    # Act
    race_car.accelerate()
    output = capfd.readouterr()

    # Assert
    assert output.out == start_engine_to_accelerate


# case-13
def test_accelerate_race_car_rapidly_when_no_nitro_and_update_current_speed():

    # Arrange
    race_car = RaceCar(
        color='DarkOrchid',
        max_speed=100,
        acceleration=10,
        tyre_friction=5
    )
    current_speed_value = 40
    race_car.start_engine()

    # Act
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()

    # Assert
    assert race_car.current_speed == current_speed_value


def test_accelerate_race_car_rapidly_when_nitro_and_update_current_speed():

    # Arrange
    race_car = RaceCar(
        color='DarkRed',
        max_speed=100,
        acceleration=15,
        tyre_friction=15
    )
    current_speed_value = 85
    race_car.start_engine()
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()
    race_car.apply_brakes()
    race_car.apply_brakes()
    race_car.apply_brakes()

    # Act
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()

    # Assert
    assert race_car.current_speed == current_speed_value


# case-14
def test_accelerate_race_car_and_update_current_speed_when_maximum():

    # Arrange
    race_car = RaceCar(
        color='DarkSalmon',
        max_speed=30,
        acceleration=10,
        tyre_friction=5
    )
    current_speed_value = 30
    race_car.start_engine()

    # Act
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()
    race_car.accelerate()

    # Assert
    assert race_car.current_speed == current_speed_value
