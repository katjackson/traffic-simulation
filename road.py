import numpy as np
import statistics as st
from car import Car

class Road():

    def __init__(self, length_of_road=1000, number_of_cars=5):
        self.number_of_cars = int(number_of_cars)
        self.length = int(length_of_road)
        self.set_of_cars = []

    def place_cars(self):
        interval = round(self.length / (self.number_of_cars))
        for number in range(self.number_of_cars):
            self.set_of_cars.append(Car(number * interval))


    def simulate_n_seconds(self, n):
        speed_data = []
        total_position_data = []

        for _ in range(n):
            temp_position_data = []

            for index, car in enumerate(self.set_of_cars):

                if index == 29:
                    index = 0

                car.choose_speed_change(self.set_of_cars[index+1])
                car.change_position()

                if _ > 28:
                    speed_data.append(car.speed)

        return speed_data, total_position_data
