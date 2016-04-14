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

    def choose_speed_change(self):
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
