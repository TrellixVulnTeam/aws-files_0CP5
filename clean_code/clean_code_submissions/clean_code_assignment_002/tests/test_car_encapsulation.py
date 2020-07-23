import pytest


# case-21
def test_car_max_speed_encapsulation_raise_attrubute_error(car):

    # Arrange
    attribute_error = "can't set attribute"

    # Act
    with pytest.raises(AttributeError) as error:
        car.max_speed = 1

    # Assert
    assert str(error.value) == attribute_error


# case-22
def test_car_acceleration_encapsulation_raise_attrubute_error(car):

    # Arrange
    attribute_error = "can't set attribute"

    # Act
    with pytest.raises(AttributeError) as error:
        car.acceleration = 2

    # Assert
    assert str(error.value) == attribute_error


# case-23
def test_car_tyre_friction_encapsulation_raise_attrubute_error(car):

    # Arrange
    attribute_error = "can't set attribute"

    # Act
    with pytest.raises(AttributeError) as error:
        car.tyre_friction = 3

    # Assert
    assert str(error.value) == attribute_error


# case-24
def test_car_current_speed_encapsulation_raise_attrubute_error(car):

    # Arrange
    attribute_error = "can't set attribute"

    # Act
    with pytest.raises(AttributeError) as error:
        car.current_speed = 4

    # Assert
    assert str(error.value) == attribute_error


# case-25
def test_car_is_engine_started_encapsulation_raise_attrubute_error(
        car):

    # Arrange
    attribute_error = "can't set attribute"

    # Act
    with pytest.raises(AttributeError) as error:
        car.is_engine_started = False

    # Assert
    assert str(error.value) == attribute_error


# case-26
def test_car_color_encapsulation_raise_attrubute_error(car):

    # Arrange
    attribute_error = "can't set attribute"

    # Act
    with pytest.raises(AttributeError) as error:
        car.color = 'Yellow'

    # Assert
    assert str(error.value) == attribute_error
