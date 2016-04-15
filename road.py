# import numpy as np
# import statistics as st
from car import Car


class Road():

    def __init__(self, length_of_road=1000, number_of_cars=30):
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
        print("this should print")
        for _ in range(n):
            temp_position_data = []
            var = 0
            for index, car in enumerate(self.set_of_cars):
                var += index
                if index == 29:
                    index = 0

                car.choose_speed_change(self.set_of_cars[index+1])
                car.change_position()
                print("OH")
                if car.car_coordinates[0] > 990:
                    print("HEY")

                if _ > 28:
                    speed_data.append(car.speed)

                temp_position_data.append(car.car_coordinates)
            total_position_data.append(temp_position_data)
            print(var)
        return speed_data, total_position_data
