import random
import numpy as np


class Car:

    def __init__(self, bumper=0):
        self.car_length = 5
        self.max_speed = 100/3
        self.acceleration = 2
        self.decceleration = 2
        self.bumper = bumper
        self.speed = 0
        self.car_coordinates = np.array([self.bumper,
                                        self.bumper + self.car_length])

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
            if random.random() < .1:
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
        return other.bumper - self.car_coordinates[1]
