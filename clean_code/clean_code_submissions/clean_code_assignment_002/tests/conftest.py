import pytest
from car import Car
from truck import Truck
from race_car import RaceCar


@pytest.fixture
def car():

    car_obj = Car(
        color='Red',
        max_speed=30,
        acceleration=10,
        tyre_friction=3
    )
    return car_obj


@pytest.fixture
def truck():
    truck_obj = Truck(
        color='Blue',
        max_speed=1,
        acceleration=1,
        tyre_friction=1,
        max_cargo_weight=1
    )
    return truck_obj


@pytest.fixture
def race_car():

    race_car_obj = RaceCar(
        color='Red',
        max_speed=30,
        acceleration=10,
        tyre_friction=3
    )
    return race_car_obj
