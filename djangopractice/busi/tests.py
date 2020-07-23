from django.test import TestCase

# Create your tests here.
#from busi.utils import *
from .utils import *
import pytest
def test_is_prime_for_prime_number_returns_true():
    # Arrange
    
    number_to_check = 8.4
    
    # Act
    result = is_prime(number_to_check)
    
    # Assert
    assert result is False
    
def test_check_email_format_with_invalid_email_raise_exception():
    with pytest.raises(Exception) as e:
            assert check_email_format('bademail.com')
        
    assert str(e.value) == "Invalid email format"
    
def test_apply_break_when_car_current_speed_is_more_than_tyre_friction():
    from .car import Car
    car = Car(color='Red',max_speed=130,acceleration=10,tyre_friction=3)
    
    car.start_engine()
    car.accelerate()
    
    car.apply_brakes()
    
    assert car.current_speed == 7
    
def test_apply_break_when_car_current_speed_is_less_than_tyre_friction():
    from .car import Car
    car = Car(color='Red',max_speed=20,acceleration=3,tyre_friction=10)
    
    car.start_engine()
    car.accelerate()
    car.apply_brakes()
    
    assert car.current_speed == 0
    
@pytest.mark.parametrize("max_speed, acceleration, tyre_friction,current_speed",[
    (130,10,3,7),(20,3,10,0)
])
def test_apply_break_when_car_is_in_motion(
    max_speed,acceleration,tyre_friction,current_speed):
    from .car import Car
    car = Car(color='Red',max_speed=max_speed,
    acceleration=acceleration, tyre_friction=tyre_friction)
    
    car.start_engine()
    car.accelerate()
    car.apply_brakes()
    
    assert car.current_speed == current_speed
'''    
@pytest.fixture
def car():
    from .car import Car
    car_obj = Car(color='Red',max_speed=30,acceleration=10,tyre_friction=3)
    return car_obj
    
def test_accelerate_car(car):
    car.start_engine()
    car.accelerate()
    
    assert car.current_speed == 10



def test_accelerate_car_more_than_max_limit(car):
    car.start_engine()
    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.accelerate()
    
    assert car.current_speed == 30


def test_apply_break_when_car_current_speed_is_more_than_tyre_friction2(car):
    # Arrange    
    car.start_engine()
    car.accelerate()
    
    # Act 
    car.apply_brakes()
    
    # Assert
    assert car.current_speed == 7'''
    
def test_my_car(car):
    assert car.max_speed == 100
    
def test_my_truck(car): 
    # Sample assert 
    assert car.max_speed == 100


    