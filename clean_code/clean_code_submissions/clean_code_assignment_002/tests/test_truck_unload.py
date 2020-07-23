import pytest
from truck import Truck


# case-
def test_unload_when_truck_in_motion_and_print_string(capfd):

    # Arrange
    truck = Truck(
        color='LightPink',
        max_speed=5,
        acceleration=4,
        tyre_friction=3,
        max_cargo_weight=100
    )
    truck.start_engine()
    truck.load(1)
    truck.accelerate()
    cannot_unload = "Cannot unload cargo during motion\n"

    # Act
    truck.unload(1)
    output = capfd.readouterr()

    # Assert
    assert output.out == cannot_unload


def test_unload_when_truck_at_rest_with_invalid_load_values_raise_error():

    # Arrange
    truck = Truck(
        color='LightSalmon',
        max_speed=5,
        acceleration=4,
        tyre_friction=3,
        max_cargo_weight=100
    )
    truck.start_engine()
    truck.load(5)
    invalid_cargo_weight = "Invalid value for cargo_weight"

    # Act
    with pytest.raises(ValueError) as error:
        truck.unload(-1)

    # Assert
    assert str(error.value) == invalid_cargo_weight


def test_unload_when_truck_at_rest_with_load_value_equal_to_available_load():

    # Arrange
    color = 'LightSeaGreen'
    max_speed = 5
    acceleration = 4
    tyre_friction = 3
    max_cargo_weight = 100

    truck = Truck(
        color=color,
        max_speed=max_speed,
        acceleration=acceleration,
        tyre_friction=tyre_friction,
        max_cargo_weight=max_cargo_weight
    )

    truck.load(2)
    load_value = 0

    # Act
    truck.unload(2)

    # Assert
    assert truck.current_load_weight == load_value


def test_unload_when_truck_at_rest_with_load_value_zero_and_update_load():

    # Arrange
    color = 'Lime'
    max_speed = 5
    acceleration = 4
    tyre_friction = 3
    max_cargo_weight = 100

    truck = Truck(
        color=color,
        max_speed=max_speed,
        acceleration=acceleration,
        tyre_friction=tyre_friction,
        max_cargo_weight=max_cargo_weight
    )

    truck.load(2)
    load_value = 2

    # Act
    truck.unload(0)

    # Assert
    assert truck.current_load_weight == load_value
