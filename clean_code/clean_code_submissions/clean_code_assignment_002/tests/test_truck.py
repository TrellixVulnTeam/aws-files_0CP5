import pytest
from truck import Truck


# case-1
def test_create_truck_object_instance_with_valid_details():
    # Arrange
    color = 'Gold'
    max_speed = 1
    acceleration = 1
    tyre_friction = 1
    max_cargo_weight = 1
    truck = Truck(
        color=color,
        max_speed=max_speed,
        acceleration=acceleration,
        tyre_friction=tyre_friction,
        max_cargo_weight=max_cargo_weight
    )

    # Act
    # Assert
    assert truck.color == color
    assert truck.max_speed == max_speed
    assert truck.acceleration == acceleration
    assert truck.tyre_friction == tyre_friction
    assert truck.max_cargo_weight == max_cargo_weight


# case-2
@pytest.mark.parametrize(
    "color, max_speed, acceleration, tyre_friction, max_cargo_weight",
    [('GoldenRod', 1, 1, 1, 10)])
def test_create_truck_object_instance_multiple_times_with_valid_details(
        color, max_speed, acceleration, tyre_friction, max_cargo_weight):
    # Arrange
    truck1 = Truck(
        color=color,
        max_speed=max_speed,
        acceleration=acceleration,
        tyre_friction=tyre_friction,
        max_cargo_weight=max_cargo_weight
    )
    truck2 = Truck(
        color=color,
        max_speed=max_speed,
        acceleration=acceleration,
        tyre_friction=tyre_friction,
        max_cargo_weight=max_cargo_weight
    )

    # Act
    # Assert
    assert truck1.color == color
    assert truck1.max_speed == max_speed
    assert truck1.acceleration == acceleration
    assert truck1.tyre_friction == tyre_friction
    assert truck1.max_cargo_weight == max_cargo_weight

    assert truck2.color == color
    assert truck2.max_speed == max_speed
    assert truck2.acceleration == acceleration
    assert truck2.tyre_friction == tyre_friction
    assert truck2.max_cargo_weight == max_cargo_weight


# case-2
@pytest.mark.parametrize(
    "color, max_speed, acceleration, tyre_friction, max_cargo_weight",
    [('Gray', 0, 1, 1, 10), ('Grey', -1, 1, 1, 5)])
def test_create_truck_object_with_invalid_max_speed_value_raise_error(
        color, max_speed, acceleration, tyre_friction, max_cargo_weight):
    # Arrange
    # Act
    with pytest.raises(ValueError) as truck:
        assert Truck(
            color=color,
            max_speed=max_speed,
            acceleration=acceleration,
            tyre_friction=tyre_friction,
            max_cargo_weight=max_cargo_weight
        )

    # Assert
    assert str(truck.value) == 'Invalid value for max_speed'


# case-3
@pytest.mark.parametrize(
    "color, max_speed, acceleration, tyre_friction, max_cargo_weight",
    [('Green', 5, 0, 1, 10), ('GreenYellow', 9, -1, 1, 5)])
def test_create_truck_object_with_invalid_acceleration_value_raise_error(
        color, max_speed, acceleration, tyre_friction, max_cargo_weight):
    # Arrange
    # Act
    with pytest.raises(ValueError) as truck:
        assert Truck(
            color=color,
            max_speed=max_speed,
            acceleration=acceleration,
            tyre_friction=tyre_friction,
            max_cargo_weight=max_cargo_weight
        )

    # Assert
    assert str(truck.value) == 'Invalid value for acceleration'


# case-4
@pytest.mark.parametrize(
    "color, max_speed, acceleration, tyre_friction, max_cargo_weight",
    [('HoneyDew', 5, 2, 0, 10), ('HotPink', 9, 3, -1, 5)])
def test_create_truck_object_with_invalid_tyre_friction_value_raise_error(
        color, max_speed, acceleration, tyre_friction, max_cargo_weight):
    # Arrange
    # Act
    with pytest.raises(ValueError) as truck:
        assert Truck(
            color=color,
            max_speed=max_speed,
            acceleration=acceleration,
            tyre_friction=tyre_friction,
            max_cargo_weight=max_cargo_weight
        )

    # Assert
    assert str(truck.value) == 'Invalid value for tyre_friction'


# case-5
@pytest.mark.parametrize(
    "color, max_speed, acceleration, tyre_friction, max_cargo_weight",
    [('IndianRed', 5, 2, 1, 0), ('Indigo', 9, 3, 2, -1)])
def test_create_truck_object_with_invalid_max_cargo_weight_value_raise_error(
        color, max_speed, acceleration, tyre_friction, max_cargo_weight):
    # Arrange
    # Act
    with pytest.raises(ValueError) as truck:
        assert Truck(
            color=color,
            max_speed=max_speed,
            acceleration=acceleration,
            tyre_friction=tyre_friction,
            max_cargo_weight=max_cargo_weight
        )

    # Assert
    assert str(truck.value) == 'Invalid value for max_cargo_weight'


# case-15
def test_truck_object_instance_create_and_engine_status():
    # Arrange
    truck = Truck(
        color='Khaki',
        max_speed=5,
        acceleration=4,
        tyre_friction=3,
        max_cargo_weight=1
    )
    engine_started = False

    # Act
    # Assert
    assert truck.is_engine_started == engine_started


# case-6
def test_start_engine_when_truck_is_at_rest_and_update_is_engine_started(
        truck):
    # Arrange
    engine_started = True

    # Act
    truck.start_engine()

    # Assert
    assert truck.is_engine_started == engine_started


# case-7
def test_stop_engine_when_truck_is_in_motion_and_update_is_engine_started(
        truck):
    # Arrange
    engine_started = False
    truck.start_engine()

    # Act
    truck.stop_engine()

    # Assert
    assert truck.is_engine_started == engine_started
