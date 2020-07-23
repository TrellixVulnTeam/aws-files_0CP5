import pytest
from car import Car


# case-1
def test_create_car_object_instance_with_valid_details():

    # Arrange
    color = 'AliceBlue'
    max_speed = 30
    acceleration = 10
    tyre_friction = 5

    # Act
    car = Car(
        color=color,
        max_speed=max_speed,
        acceleration=acceleration,
        tyre_friction=tyre_friction
    )

    # Assert
    assert car.color == color
    assert car.max_speed == max_speed
    assert car.acceleration == acceleration
    assert car.tyre_friction == tyre_friction


# case-2
@pytest.mark.parametrize("color, max_speed, acceleration, tyre_friction", [
    ('AntiqueWhite', 1, 1, 1)])
def test_create_car_object_instance_multiple_times_with_valid_details(
        color, max_speed, acceleration, tyre_friction):

    # Arrange

    # Act
    car_1 = Car(
        color=color,
        max_speed=max_speed,
        acceleration=acceleration,
        tyre_friction=tyre_friction
    )
    car_2 = Car(
        color=color,
        max_speed=max_speed,
        acceleration=acceleration,
        tyre_friction=tyre_friction
    )

    # Assert
    assert car_1.color == color
    assert car_1.max_speed == max_speed
    assert car_1.acceleration == acceleration
    assert car_1.tyre_friction == tyre_friction

    assert car_2.color == color
    assert car_2.max_speed == max_speed
    assert car_2.acceleration == acceleration
    assert car_2.tyre_friction == tyre_friction


# case-3
@pytest.mark.parametrize("color, max_speed, acceleration, tyre_friction", [
    ('Aqua', 0, 10, 15), ('Aquamarine', -1, 10, 5)])
def test_create_car_object_with_invalid_max_speed_value_raise_error(
        color, max_speed, acceleration, tyre_friction):

    # Arrange
    invalid_max_speed = 'Invalid value for max_speed'

    # Act
    with pytest.raises(ValueError) as car:
        assert Car(
            color=color,
            max_speed=max_speed,
            acceleration=acceleration,
            tyre_friction=tyre_friction
        )

    # Assert
    assert str(car.value) == invalid_max_speed


# case-3
@pytest.mark.parametrize("color, max_speed, acceleration, tyre_friction", [
    ('Azure', 30, 0, 5), ('Beige', 30, -1, 5)])
def test_create_car_object_with_invalid_acceleration_value_raise_error(
        color, max_speed, acceleration, tyre_friction):

    # Arrange
    invalid_acceleration = 'Invalid value for acceleration'

    # Act
    with pytest.raises(ValueError) as car:
        assert Car(
            color=color,
            max_speed=max_speed,
            acceleration=acceleration,
            tyre_friction=tyre_friction
        )

    # Assert
    assert str(car.value) == invalid_acceleration


# case-3
@pytest.mark.parametrize("color, max_speed, acceleration, tyre_friction", [
    ('Bisque', 30, 10, 0), ('Black', 30, 10, -1)])
def test_create_car_object_with_invalid_tyre_friction_value_raise_error(
        color, max_speed, acceleration, tyre_friction):

    # Arrange
    invalid_tyre_friction = 'Invalid value for tyre_friction'

    # Act
    with pytest.raises(ValueError) as car:
        assert Car(
            color=color,
            max_speed=max_speed,
            acceleration=acceleration,
            tyre_friction=tyre_friction
        )

    # Assert
    assert str(car.value) == invalid_tyre_friction


# case-20
def test_car_object_instance_create_and_engine_status():

    # Arrange
    car = Car(
        color='BlanchedAlmond',
        max_speed=130,
        acceleration=10,
        tyre_friction=3
    )
    engine_started = False

    # Act

    # Assert
    assert car.is_engine_started == engine_started


# case-9
def test_start_engine_when_car_is_in_rest_and_update_is_engine_started(car):

    # Arrange
    engine_started = True

    # Act
    car.start_engine()

    # Assert
    assert car.is_engine_started == engine_started


# case-10
def test_stop_engine_when_car_is_in_motion_and_update_is_engine_started(car):

    # Arrange
    engine_started = False
    car.start_engine()

    # Act
    car.stop_engine()

    # Assert
    assert car.is_engine_started == engine_started
