from car import Car


# case-18
def test_sound_horn_when_car_engine_started_and_return_car_sound(capfd):

    # Arrange
    car = Car(
        color='Coral',
        max_speed=130,
        acceleration=10,
        tyre_friction=3
    )
    sound = "Beep Beep\n"
    car.start_engine()

    # Act
    car.sound_horn()
    output = capfd.readouterr()

    # Assert
    assert output.out == sound


# case-19
def test_sound_horn_when_car_engine_stoped_and_print_start_engine(capfd):

    # Arrange
    car = Car(
        color='CornflowerBlue',
        max_speed=130,
        acceleration=10,
        tyre_friction=3
    )
    start_engine_to_sound = "Start the engine to sound_horn\n"

    # Act
    car.sound_horn()
    output = capfd.readouterr()

    # Assert
    assert output.out == start_engine_to_sound
