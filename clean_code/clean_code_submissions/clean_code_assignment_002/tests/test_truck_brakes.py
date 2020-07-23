from truck import Truck


# case-11
def test_apply_brakes_when_truck_current_speed_is_less_than_tyre_friction():

    # Arrange
    truck = Truck(
        color='LightCyan',
        max_speed=5,
        acceleration=3,
        tyre_friction=4,
        max_cargo_weight=1
    )
    truck.start_engine()
    truck.accelerate()

    # Act
    truck.apply_brakes()
    current_speed_value = 0

    # Assert
    assert truck.current_speed == current_speed_value


# case-12
def test_apply_brakes_when_truck_current_speed_is_more_than_tyre_friction():

    # Arrange
    truck = Truck(
        color='LightGreen',
        max_speed=5,
        acceleration=4,
        tyre_friction=3,
        max_cargo_weight=1
    )
    truck.start_engine()
    truck.accelerate()

    # Act
    truck.apply_brakes()
    current_speed_value = 1

    # Assert
    assert truck.current_speed == current_speed_value
