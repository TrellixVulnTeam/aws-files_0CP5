import pytest
from race_car import RaceCar


# case-1
def test_create_race_car_object_instance_with_valid_details():

    # Arrange
    color = 'Cornsilk'
    max_speed = 30
    acceleration = 10
    tyre_friction = 5

    # Act
    race_car = RaceCar(
        color=color,
        max_speed=max_speed,
        acceleration=acceleration,
        tyre_friction=tyre_friction
    )

    # Assert
    assert race_car.color == color
    assert race_car.max_speed == max_speed
    assert race_car.acceleration == acceleration
    assert race_car.tyre_friction == tyre_friction


# case-2
@pytest.mark.parametrize(
    "color, max_speed, acceleration, tyre_friction",
    [('Crimson', 1, 1, 1)])
def test_create_race_car_object_instance_multiple_times_with_valid_details(
        color, max_speed, acceleration, tyre_friction):

    # Arrange

    # Act
    race_car_1 = RaceCar(
        color=color,
        max_speed=max_speed,
        acceleration=acceleration,
        tyre_friction=tyre_friction
    )

    race_car_2 = RaceCar(
        color=color,
        max_speed=max_speed,
        acceleration=acceleration,
        tyre_friction=tyre_friction
    )

    # Assert
    assert race_car_1.color == color
    assert race_car_1.max_speed == max_speed
    assert race_car_1.acceleration == acceleration
    assert race_car_1.tyre_friction == tyre_friction

    assert race_car_2.color == color
    assert race_car_2.max_speed == max_speed
    assert race_car_2.acceleration == acceleration
    assert race_car_2.tyre_friction == tyre_friction


# case-3
@pytest.mark.parametrize(
    "color, max_speed, acceleration, tyre_friction",
    [('cyan', 0, 10, 15), ('DarkBlue', -1, 10, 5)])
def test_create_race_car_object_with_invalid_max_speed_value_raise_error(
        color, max_speed, acceleration, tyre_friction):

    # Arrange
    invalid_max_speed = 'Invalid value for max_speed'

    # Act
    with pytest.raises(ValueError) as race_car:
        assert RaceCar(
            color=color,
            max_speed=max_speed,
            acceleration=acceleration,
            tyre_friction=tyre_friction
        )

    # Assert
    assert str(race_car.value) == invalid_max_speed


# case-3
@pytest.mark.parametrize(
    "color, max_speed, acceleration, tyre_friction",
    [('DarkCyan', 30, 0, 5), ('DarkGoldenRod', 30, -1, 5)])
def test_create_race_car_object_with_invalid_acceleration_value_raise_error(
        color, max_speed, acceleration, tyre_friction):

    # Arrange
    invalid_acceleration = 'Invalid value for acceleration'

    # Act
    with pytest.raises(ValueError) as race_car:
        assert RaceCar(
            color=color,
            max_speed=max_speed,
            acceleration=acceleration,
            tyre_friction=tyre_friction
        )

    # Assert
    assert str(race_car.value) == invalid_acceleration


# case-3
@pytest.mark.parametrize(
    "color, max_speed, acceleration, tyre_friction",
    [('DarkGray', 30, 10, 0), ('DarkGrey', 30, 10, -1)])
def test_create_race_car_object_with_invalid_tyre_friction_value_raise_error(
        color, max_speed, acceleration, tyre_friction):

    # Arrange
    invalid_tyre_friction = 'Invalid value for tyre_friction'

    # Act
    with pytest.raises(ValueError) as race_car:
        assert RaceCar(
            color=color,
            max_speed=max_speed,
            acceleration=acceleration,
            tyre_friction=tyre_friction
        )

    # Assert
    assert str(race_car.value) == invalid_tyre_friction


# case-9
def test_start_engine_when_race_car_at_rest_and_update_is_engine_started(
        race_car):

    # Arrange
    engine_started = True

    # Act
    race_car.start_engine()

    # Assert
    assert race_car.is_engine_started == engine_started


# case-10
def test_stop_engine_when_race_car_is_in_motion_and_update_is_engine_started(
        race_car):

    # Arrange
    engine_started = False
    race_car.start_engine()

    # Act
    race_car.stop_engine()

    # Assert
    assert race_car.is_engine_started == engine_started


# case-20
def test_race_car_object_instance_create_and_engine_status():

    # Arrange
    race_car = RaceCar(
        color='DarkGreen',
        max_speed=130,
        acceleration=10,
        tyre_friction=3
    )
    engine_started = False

    # Act

    # Assert
    assert race_car.is_engine_started == engine_started


def test_race_car_object_instance_create_and_nitro_status():

    # Arrange
    race_car = RaceCar(
        color='DarkKhaki',
        max_speed=130,
        acceleration=10,
        tyre_friction=3
    )
    nitro_value = 0

    # Act

    # Assert
    assert race_car.nitro == nitro_value
