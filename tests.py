from car import Car
from road import Road

test_car = Car()
test_road = Road()


"""
ROAD CLASS TESTS BELOW
"""


def test_init_length():
    assert test_road.length == 1000
    assert test_road.number_of_cars == 5
    assert test_road.set_of_cars == []


def test_place_cars_length():
    test_road.place_cars()
    assert len(test_road.set_of_cars) == 5


def test_place_cars_type():
    test_road.place_cars()
    assert isinstance(test_road.set_of_cars[0], Car)


def test_place_cars_positioning():
    test_road.place_cars()
    assert test_road.set_of_cars[0].car_coordinates[0] == 0
    assert test_road.set_of_cars[1].car_coordinates[0] == int(round(1000/5))
    assert test_road.set_of_cars[4].car_coordinates[0] == int(4*round(1000/5))


"""
CAR CLASS TESTS BELOW
"""


def test_car_is_5m_long():
    assert test_car.car_length == 5


def test_coordinates():
    test_car_2 = Car(3)
    print(test_car_2.car_coordinates)
    assert test_car_2.car_coordinates[0] == 3
    assert test_car_2.car_coordinates[1] == 7


def test_set_max_speed():
    assert test_car.max_speed == int(round(100/3))


def test_accelerate_max():
    test_car.speed = 100/3 - 1
    test_car.accelerate()
    assert test_car.speed == int(round(100/3))


def test_accelerate():
    test_car.speed = 5
    test_car.accelerate()
    assert test_car.speed == 7


def test_decelerate():
    test_car.speed = 5
    test_car.decelerate()
    assert test_car.speed == 3


def test_decelerate_min():
    test_car.speed = 1
    test_car.decelerate()
    assert test_car.speed == 0


def test_move_car():
    test_car.speed = 2
    test_car.change_position()
    assert test_car.car_coordinates[0] == 2
    assert test_car.car_coordinates[1] == 6


def test_move_car_end_of_track():
    test_car = Car(990)
    test_car.speed = 30
    test_car.change_position()
    assert test_car.car_coordinates[0] == 20
    assert test_car.car_coordinates[1] == 24


def test_follow_distance():
    test_car = Car()
    test_car_two = Car(10)
    assert test_car.get_space_available(test_car_two) == 6


def test_choose_speed_braaaaake():
    test_car = Car()
    test_car.speed = 10
    test_car_two = Car(10)
    test_car_two.speed = 6
    test_car.set_new_speed(test_car_two)
    assert test_car.speed == 0


def test_choose_speed_slow():
    test_car = Car()
    test_car.speed = 10
    test_car_two = Car(14)
    test_car_two.speed = 6
    test_car.set_new_speed(test_car_two)
    assert test_car.speed == 8


def test_choose_speed_steady():
    test_car = Car()
    test_car.speed = 10
    test_car_two = Car(14)
    test_car_two.speed = 10
    test_car.set_new_speed(test_car_two)
    assert test_car.speed == 10


def test_choose_speed_steady_slow():
    test_car = Car()
    test_car.speed = 10
    test_car_two = Car(14)
    test_car_two.speed = 8
    test_car.set_new_speed(test_car_two)
    assert test_car.speed == 8


def test_choose_speed_steady_fast():
    test_car = Car()
    test_car.speed = 10
    test_car_two = Car(15)
    test_car_two.speed = 12
    test_car.set_new_speed(test_car_two)
    assert test_car.speed == 12
