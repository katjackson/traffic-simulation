from car import Car


class Road:

    def __init__(self, number_of_cars,
                 length_of_road=1000, slow_percentage=.1):
        self.number_of_cars = number_of_cars
        self.length = length_of_road
        self.set_of_cars = []
        self.drive_var = slow_percentage

    def place_cars(self):
        interval = round(self.length / (self.number_of_cars))
        for number in list(range(self.number_of_cars))[::-1]:
            self.set_of_cars.append(Car(number * interval))

    def check_position(self, car, other):
        # STILL NEEDS FIXING
        gap = other.car_coordinates[0] - car.car_coordinates[-1]
        if (gap <= 0) or (gap > self.length_of_road-car.vehicle_size):
            car.car_coordinates = car.car_coordinates + (
                car.car_coordinates[-1] - (other.car_coordinates[0] + 1))
            car.speed = 0

    def check_end_of_lap(self, car):
        car.car_coordinates = (car.car_coordinates %
                               self.length)

    def set_tail_distance(self, car, other):
        if car.car_coordinates[-1] > other.car_coordinates[0]:
            return ((self.length + other.car_coordinates[0]) -
                    (car.car_coordinates[-1] + car.speed))
        return (other.car_coordinates[0] -
                (car.car_coordinates[-1] + car.speed))

    def simulate_n_seconds(self, n):
        speed_data = []
        position_data = []

        for _ in range(n):
            for index, car in enumerate(self.set_of_cars):
                if index == len(self.set_of_cars) - 1:
                    index = -1

                td = self.set_tail_distance(car, self.set_of_cars[index+1])
                car.set_new_speed(self.set_of_cars[index+1], td)
                car.change_position()
                self.check_end_of_lap(car)
                self.check_position(car, self.set_of_cars[index+1])
                self.check_end_of_lap(car)

                if _ > n/2:
                    speed_data.append(car.speed)

                position_data.append(car.car_coordinates)

        return speed_data, position_data
