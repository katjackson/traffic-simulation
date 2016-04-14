# import random
import numpy as np


class Car:

    def __init__(self, bumper=0):
        self.car_length = 5
        self.max_speed = int(round(100/3))
        self.acceleration = 2
        self.decceleration = 2
        self.speed = 0
        self.car_coordinates = np.array([bumper,
                                        bumper + self.car_length])

    def choose_speed_change(self, other):

        follow_distance = self.get_follow_distance(other)

        if self.speed - follow_distance == 0:
            if other.speed < self.speed:
                self.deccelerate()
            elif other.speed > self.speed:
                self.accelerate()

        elif self.speed - follow_distance > 2:
            self.speed = 0

        elif 0 < self.speed - follow_distance <= 2:
            self.deccelerate()

        else:
            if False:
                self.deccelerate()
            else:
                self.accelerate()

    def accelerate(self):
        self.speed += 2
        if self.speed > self.max_speed:
            self.speed = self.max_speed

    def deccelerate(self):
        self.speed -= 2
        if self.speed < 0:
            self.speed = 0

    def change_position(self):
        self.car_coordinates += self.speed
        self.car_coordinates = self.car_coordinates % 1000

    def get_follow_distance(self, other):
        if other.car_coordinates[0] - self.car_coordinates[1] < 0:
            return 1000 + other.car_coordinates[0] - self.car_coordinates[1]
        return other.car_coordinates[0] - self.car_coordinates[1]
