from car import Car


# case-15
def test_apply_brakes_to_car_and_update_current_speed():

    # Arrange
    car = Car(
        color='CadetBlue',
        max_speed=100,
        acceleration=10,
        tyre_friction=10
    )
    current_speed_value = 0
    car.start_engine()
    car.accelerate()
    car.accelerate()
    car.accelerate()

    # Act
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()

    # Assert
    assert car.current_speed == current_speed_value


# case-16
def test_apply_brakes_when_car_current_speed_is_less_than_tyre_friction():

    # Arrange
    car = Car(
        color='Chartreuse',
        max_speed=20,
        acceleration=9,
        tyre_friction=10
    )
    current_speed_value = 0
    car.start_engine()
    car.accelerate()

    # Act
    car.apply_brakes()

    # Assert
    assert car.current_speed == current_speed_value


# case-17
def test_apply_brakes_when_car_current_speed_is_more_than_tyre_friction():

    # Arrange
    car = Car(
        color='Chocolate',
        max_speed=130,
        acceleration=10,
        tyre_friction=3
    )
    current_speed_value = 1
    car.start_engine()
    car.accelerate()

    # Act
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()

    # Assert
    assert car.current_speed == current_speed_value
