import random


class Car:

    def __init__(self, bumper=0):
        self.max_speed = 33  # meters/second
        self.car_length = 5  # meters
        self.acceleration = 2  # meters/second^2
        self.deceleration = 2  # meters/second^2
        self.speed = 0  # meters/second
        self.car_coordinates = [bumper, bumper + self.car_length - 1]

    def set_new_speed(self, other):
        tailing_distance_left = (
            self.get_space_available(other) - self.speed)

        if tailing_distance_left > 0:
            # random accel/decel
            self.drive_plenty_of_room(other)

        elif tailing_distance_left == 0:
            # match speed
            self.drive_tail_other(other)

        elif tailing_distance_left >= -2:
            # too close, must brake
            self.decelerate()

        elif tailing_distance_left < -2:
            # way too close and too fast, must stop
            self.speed = 0

    def drive_plenty_of_room(self, other):
        # ensure that car didn't somehow collide with other
        if self.get_follow_distance(other) <= 2:
            self.speed = 0
        elif random.random() < 0.1:
            self.decelerate()
        else:
            self.accelerate()

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

    def deccelerate(self):
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
