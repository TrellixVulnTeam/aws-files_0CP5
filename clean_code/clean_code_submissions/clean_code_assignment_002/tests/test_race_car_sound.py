from race_car import RaceCar


# case-18
def test_sound_horn_when_race_car_engine_started_and_return_race_car_sound(
        capfd):

    # Arrange
    race_car = RaceCar(
        color='FireBrick',
        max_speed=130,
        acceleration=10,
        tyre_friction=3
    )
    sound = "Peep Peep\nBeep Beep\n"
    race_car.start_engine()

    # Act
    race_car.sound_horn()
    output = capfd.readouterr()

    # Assert
    assert output.out == sound


# case-19
def test_sound_horn_when_race_car_engine_stoped_and_print_start_engine(capfd):

    # Arrange
    race_car = RaceCar(
        color='FloralWhite',
        max_speed=130,
        acceleration=10,
        tyre_friction=3
    )
    start_engine_to_sound = "Start the engine to sound_horn\n"

    # Act
    race_car.sound_horn()
    output = capfd.readouterr()

    # Assert
    assert output.out == start_engine_to_sound
