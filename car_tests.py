from car import Car
import numpy as np

test_car = Car()


def test_car_is_5m_long():
    assert test_car.car_length == 5


def test_coordinates():
    test_car_2 = Car(3)
    assert test_car_2.car_coordinates[0] == 3
    assert test_car_2.car_coordinates[1] == 8


def test_set_max_speed():
    assert test_car.max_speed == 100/3


def test_accelerate_max():
    test_car.speed = 100/3 - 1
    test_car.accelerate()
    assert test_car.speed == 100/3


def test_accelerate():
    test_car.speed = 5
    test_car.accelerate()
    assert test_car.speed == 7


def test_deccelerate():
    test_car.speed = 5
    test_car.deccelerate()
    assert test_car.speed == 3


def test_deccelerate_min():
    test_car.speed = 1
    test_car.deccelerate()
    assert test_car.speed == 0


def test_move_car():
    test_car.speed = 2
    test_car.change_position()
    assert test_car.car_coordinates[0] == 2
    assert test_car.car_coordinates[1] == 7
