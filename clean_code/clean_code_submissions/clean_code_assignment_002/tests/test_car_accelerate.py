from car import Car


# case-11
def test_accelerate_car_when_engine_started_and_update_current_speed():

    # Arrange
    car = Car(
        color='Blue',
        max_speed=20,
        acceleration=10,
        tyre_friction=5
    )
    current_speed_value = 10
    car.start_engine()

    # Act
    car.accelerate()

    # Assert
    assert car.current_speed == current_speed_value


# case-12
def test_accelerate_car_when_engine_stoped_and_print_start_engine(capfd):

    # Arrange
    car = Car(
        color='BlueViolet',
        max_speed=20,
        acceleration=10,
        tyre_friction=5
    )
    start_engine_to_accelerate = "Start the engine to accelerate\n"

    # Act
    car.accelerate()
    output = capfd.readouterr()

    # Assert
    assert output.out == start_engine_to_accelerate


# case-13
def test_accelerate_car_multiple_times_and_update_current_speed():

    # Arrange
    car = Car(
        color='Brown',
        max_speed=100,
        acceleration=10,
        tyre_friction=5
    )
    current_speed_value = 40
    car.start_engine()

    # Act
    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.accelerate()

    # Assert
    assert car.current_speed == current_speed_value


# case-14
def test_accelerate_car_and_update_current_speed_when_maximum():

    # Arrange
    car = Car(
        color='BurlyWood',
        max_speed=30,
        acceleration=10,
        tyre_friction=5
    )
    current_speed_value = 30
    car.start_engine()

    # Act
    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.accelerate()

    # Assert
    assert car.current_speed == current_speed_value
