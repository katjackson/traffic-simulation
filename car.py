# from road import Road
import random
import numpy as np


class Car:

    def __init__(self, rear_coordinate=0):
        self.acceleration = 2  # to change speed (can be up or down)
        self.desired_speed = 33  # speed limit
        self.vehicle_size = 5  # car length
        self.speed = 0  # units to move the vehicle each turn
        self.slow_chance = 0.1
        self.car_coordinates = np.array([
                *range(rear_coordinate, rear_coordinate +
                                        self.vehicle_size)])

    def change_position(self):
        self.car_coordinates += self.speed

    def set_new_speed(self, other, tail_distance):
        if isinstance(type(self), Commercial):
            tail_distance -= self.speed
        if tail_distance == 0:  # match speed
            self.drive_tail_other(other)
        elif tail_distance > 0:  # random accel/decel
            self.drive_random()
        else:
            self.decelerate()  # must slow

    def drive_tail_other(self, other):
        # go the same speed as the car in front
        if self.speed > other.speed:
            self.decelerate()
        elif self.speed < other.speed:
            self.accelerate()

    def drive_random(self):
        # ensure that car didn't somehow collide with other
        if random.random() < self.slow_chance:
            self.decelerate()
        else:
            self.accelerate()

    def accelerate(self):
        self.speed += self.acceleration
        if self.speed > self.desired_speed:
            self.speed = self.desired_speed

    def decelerate(self):
        self.speed -= self.acceleration
        if self.speed < 0:
            self.speed = 0


class Aggressive(Car):

    def __init__(self, rear_coordinate=0):
        self.acceleration = 5  # to change speed (can be up or down)
        self.desired_speed = 39  # speed limit
        self.vehicle_size = 5  # car length
        self.speed = 0  # units to move the vehicle each turn
        self.slow_chance = 0.05
        self.car_coordinates = np.array([
                *range(rear_coordinate, rear_coordinate +
                                        self.vehicle_size)])


class Commercial(Car):

    def __init__(self, rear_coordinate=0):
        self.acceleration = 1  # to change speed (can be up or down)
        self.desired_speed = 28  # speed limit
        self.vehicle_size = 25  # car length
        self.speed = 0  # units to move the vehicle each turn
        self.slow_chance = 0.1
        self.car_coordinates = np.array([
                *range(rear_coordinate, rear_coordinate +
                                        self.vehicle_size)])
