import pytest


# case-21
def test_race_car_max_speed_encapsulation_raise_attrubute_error(
        race_car):

    # Arrange
    attribute_error = "can't set attribute"

    # Act
    with pytest.raises(AttributeError) as error:
        race_car.max_speed = 6

    # Assert
    assert str(error.value) == attribute_error


# case-22
def test_race_car_acceleration_encapsulation_raise_attrubute_error(
        race_car):

    # Arrange
    attribute_error = "can't set attribute"

    # Act
    with pytest.raises(AttributeError) as error:
        race_car.acceleration = 7

    # Assert
    assert str(error.value) == attribute_error


# case-23
def test_race_car_tyre_friction_encapsulation_raise_attrubute_error(
        race_car):

    # Arrange
    attribute_error = "can't set attribute"

    # Act
    with pytest.raises(AttributeError) as error:
        race_car.tyre_friction = 8

    # Assert
    assert str(error.value) == attribute_error


# case-24
def test_race_car_current_speed_encapsulation_raise_attrubute_error(
        race_car):

    # Arrange
    attribute_error = "can't set attribute"

    # Act
    with pytest.raises(AttributeError) as error:
        race_car.current_speed = 9

    # Assert
    assert str(error.value) == attribute_error


# case-25
def test_race_car_is_engine_started_encapsulation_raise_attrubute_error(
        race_car):

    # Arrange
    attribute_error = "can't set attribute"

    # Act
    with pytest.raises(AttributeError) as error:
        race_car.is_engine_started = False

    # Assert
    assert str(error.value) == attribute_error


# case-26
def test_race_car_color_encapsulation_raise_attrubute_error(race_car):

    # Arrange
    attribute_error = "can't set attribute"

    # Act
    with pytest.raises(AttributeError) as error:
        race_car.color = 'DodgerBlue'

    # Assert
    assert str(error.value) == attribute_error


# case-26
def test_race_car_nitro_encapsulation_raise_attrubute_error(
        race_car):

    # Arrange
    attribute_error = "can't set attribute"

    # Act
    with pytest.raises(AttributeError) as error:
        race_car.nitro = 10

    # Assert
    assert str(error.value) == attribute_error
