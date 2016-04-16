import random


class Road():

    def __init__(self, length_of_road=1000,
                 number_of_cars=5, slow_percentage=.1):
        self.number_of_cars = int(number_of_cars)
        self.length = int(length_of_road)
        self.set_of_cars = []
        self.drive_var = slow_percentage

    def place_cars(self):
        interval = round(self.length / (self.number_of_cars))
        for number in range(self.number_of_cars):
            self.set_of_cars.append(Car(number * interval))

    def adjust_driver_behavior(self, car, other):
        # ensure that car didn't somehow collide with other
        if car.get_space_available(other) <= 2:
            car.speed = 0
        elif random.random() < self.drive_var:
            car.decelerate()
        else:
            car.accelerate()

    def simulate_n_seconds(self, n):
        speed_data = []
        total_position_data = []

        for _ in range(n):
            temp_position_data = []

            for index, car in enumerate(self.set_of_cars):
                if index == 29:
                    index = 0

                car.set_new_speed(self.set_of_cars[index+1], self)
                car.change_position()

                if _ > 28:
                    speed_data.append(car.speed)

                temp_position_data.append(car.car_coordinates)

            total_position_data.append(temp_position_data)
        return speed_data, total_position_data


class Car:

    def __init__(self, bumper=0):
        self.max_speed = 33  # meters/second
        self.car_length = 5  # meters
        self.acceleration = 2  # meters/second^2
        self.deceleration = 2  # meters/second^2
        self.speed = 0  # meters/second
        self.car_coordinates = [bumper, bumper + self.car_length - 1]

    def set_new_speed(self, other, road):
        tailing_distance_left = (
            self.get_space_available(other) - self.speed)

        if tailing_distance_left > 0:
            # random accel/decel
            road.adjust_driver_behavior(self, other)

        elif tailing_distance_left == 0:
            # match speed
            self.drive_tail_other(other)

        elif tailing_distance_left >= -2:
            # too close, must brake
            self.decelerate()

        elif tailing_distance_left < -2:
            # way too close and too fast, must stop
            self.speed = 0

    def drive_tail_other(self, other):
        # go the same speed as the car in front
        if self.speed > other.speed:
            self.decelerate()

        elif self.speed < other.speed:
            self.accelerate()

    def accelerate(self):
        self.speed += self.acceleration
        if self.speed > self.max_speed:
            self.speed = self.max_speed

    def decelerate(self):
        self.speed -= self.deceleration
        if self.speed < 0:
            self.speed = 0

    def change_position(self):
        self.car_coordinates[0] += self.speed
        self.car_coordinates[1] += self.speed

        if self.car_coordinates[0] >= 1000:
            self.car_coordinates[0] -= 1000
        if self.car_coordinates[1] >= 1000:
            self.car_coordinates[1] -= 1000

    def get_space_available(self, other):
        if other.car_coordinates[0] - self.car_coordinates[1] < 0:
            return (1000 + other.car_coordinates[0] - self.car_coordinates[1])
        return other.car_coordinates[0] - self.car_coordinates[1]
