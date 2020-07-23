from truck import Truck


# case-8
def test_accelerate_truck_when_engine_started_and_update_current_speed():

    # Arrange
    truck = Truck(
        color='LawGreen',
        max_speed=1,
        acceleration=1,
        tyre_friction=1,
        max_cargo_weight=1
    )
    truck.start_engine()
    current_speed_value = 1

    # Act
    truck.accelerate()

    # Assert
    assert truck.current_speed == current_speed_value


# case-9
def test_accelerate_truck_when_engine_stoped_and_print_start_engine_(capfd):

    # Arrange
    truck = Truck(
        color='LemonChiffon',
        max_speed=1,
        acceleration=1,
        tyre_friction=1,
        max_cargo_weight=1
    )
    start_engine_to_accelerate = "Start the engine to accelerate\n"

    # Act
    truck.accelerate()
    output = capfd.readouterr()

    # Assert
    assert output.out == start_engine_to_accelerate


# case-10
def test_accelerate_truck_and_update_current_speed_when_maximum():

    # Arrange
    truck = Truck(
        color='LightBlue',
        max_speed=9,
        acceleration=3,
        tyre_friction=1,
        max_cargo_weight=1
    )
    truck.start_engine()

    # Act
    truck.accelerate()
    truck.accelerate()
    truck.accelerate()
    truck.accelerate()
    current_speed_value = 9

    # Assert
    assert truck.current_speed == current_speed_value
