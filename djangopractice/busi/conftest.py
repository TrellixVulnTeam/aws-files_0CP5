import pytest
@pytest.fixture
def car():
    from .car import Car
    car_obj = Car(color='Red',max_speed=100,acceleration=10,tyre_friction=3)
    return car_obj