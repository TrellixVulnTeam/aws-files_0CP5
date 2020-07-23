from truck import Truck


# case-13
def test_sound_horn_when_truck_engine_started_and_return_car_sound(capfd):

    # Arrange
    truck = Truck(
        color='LimeGreen',
        max_speed=5,
        acceleration=4,
        tyre_friction=3,
        max_cargo_weight=1
    )
    truck.start_engine()
    sound = "Honk Honk\n"

    # Act
    truck.sound_horn()
    output = capfd.readouterr()

    # Assert
    assert output.out == sound


# case-14
def test_sound_horn_when_truck_engine_stoped_and_print_start_engine(capfd):

    # Arrange
    truck = Truck(
        color='Linen',
        max_speed=5,
        acceleration=4,
        tyre_friction=3,
        max_cargo_weight=1
    )
    start_engine_to_sound = "Start the engine to sound_horn\n"

    # Act
    truck.sound_horn()
    output = capfd.readouterr()

    # Assert
    assert output.out == start_engine_to_sound
