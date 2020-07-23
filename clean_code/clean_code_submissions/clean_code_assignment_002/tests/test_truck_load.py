import pytest
from truck import Truck


# case-
def test_load_when_truck_in_motion_and_print_string(capfd):

    # Arrange
    truck = Truck(
        color='Magenta',
        max_speed=5,
        acceleration=4,
        tyre_friction=3,
        max_cargo_weight=100
    )
    truck.start_engine()
    truck.accelerate()
    cannot_load = "Cannot load cargo during motion\n"

    # Act
    truck.load(1)
    output = capfd.readouterr()

    # Assert
    assert output.out == cannot_load


def test_load_when_truck_not_in_motion_with_invalid_load_values_raise_error():

    # Arrange
    truck = Truck(
        color='Maroon',
        max_speed=5,
        acceleration=4,
        tyre_friction=3,
        max_cargo_weight=100
    )
    truck.start_engine()
    invalid_cargo_weight = "Invalid value for cargo_weight"

    # Act
    with pytest.raises(ValueError) as error:
        truck.load(-1)

    # Assert
    assert str(error.value) == invalid_cargo_weight


def test_load_when_truck_at_rest_and_print_string_when_load_maximum(capfd):

    # Arrange
    color = 'MediumBlue'
    max_speed = 5
    acceleration = 4
    tyre_friction = 3
    max_cargo_weight = 1

    truck = Truck(
        color=color,
        max_speed=max_speed,
        acceleration=acceleration,
        tyre_friction=tyre_friction,
        max_cargo_weight=max_cargo_weight
    )
    cannot_load_more = ("Cannot load cargo more than max limit: {}\n"
                        .format(max_cargo_weight))

    # Act
    truck.load(2)
    output = capfd.readouterr()

    # Assert
    assert output.out == cannot_load_more


def test_load_when_truck_at_rest_with_valid_load_values_and_update_load():

    # Arrange
    color = 'MintCream'
    max_speed = 5
    acceleration = 4
    tyre_friction = 3
    max_cargo_weight = 1

    truck = Truck(
        color=color,
        max_speed=max_speed,
        acceleration=acceleration,
        tyre_friction=tyre_friction,
        max_cargo_weight=max_cargo_weight
    )
    load_value = 1

    # Act
    truck.load(1)

    # Assert
    assert truck.current_load_weight == load_value


def test_load_when_truck_at_rest_with_load_value_to_zero_and_update_load():

    # Arrange
    color = 'MistyRose'
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
    load_value = 0

    # Act
    truck.load(0)

    # Assert
    assert truck.current_load_weight == load_value
