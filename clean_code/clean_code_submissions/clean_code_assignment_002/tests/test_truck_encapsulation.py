import pytest


# case-21
def test_truck_max_speed_encapsulation_raise_attrubute_error(truck):

    # Arrange
    attribute_error = "can't set attribute"

    # Act
    with pytest.raises(AttributeError) as error:
        truck.max_speed = 11

    # Assert
    assert str(error.value) == attribute_error


# case-22
def test_truck_acceleration_encapsulation_raise_attrubute_error(truck):

    # Arrange
    attribute_error = "can't set attribute"

    # Act
    with pytest.raises(AttributeError) as error:
        truck.acceleration = 12

    # Assert
    assert str(error.value) == attribute_error


# case-23
def test_truck_tyre_friction_encapsulation_raise_attrubute_error(truck):

    # Arrange
    attribute_error = "can't set attribute"

    # Act
    with pytest.raises(AttributeError) as error:
        truck.tyre_friction = 13

    # Assert
    assert str(error.value) == attribute_error


# case-24
def test_truck_current_speed_encapsulation_raise_attrubute_error(truck):

    # Arrange
    attribute_error = "can't set attribute"

    # Act
    with pytest.raises(AttributeError) as error:
        truck.current_speed = 14

    # Assert
    assert str(error.value) == attribute_error


# case-25
def test_truck_is_engine_started_encapsulation_raise_attrubute_error(truck):

    # Arrange
    attribute_error = "can't set attribute"

    # Act
    with pytest.raises(AttributeError) as error:
        truck.is_engine_started = False

    # Assert
    assert str(error.value) == attribute_error


# case-26
def test_truck_color_encapsulation_raise_attrubute_error(truck):

    # Arrange
    attribute_error = "can't set attribute"

    # Act
    with pytest.raises(AttributeError) as error:
        truck.color = 'Olive'

    # Assert
    assert str(error.value) == attribute_error


# case-26
def test_truck_max_cargo_weight_encapsulation_raise_attrubute_error(truck):

    # Arrange
    attribute_error = "can't set attribute"

    # Act
    with pytest.raises(AttributeError) as error:
        truck.max_cargo_weight = 50

    # Assert
    assert str(error.value) == attribute_error
