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
        if (car.car_coordinates[-1] in
            list(range(other.car_coordinates[0],
                       other.car_coordinates[0]+car.speed+1))):
            car.car_coordinates = car.car_coordinates - (
                car.car_coordinates[-1] - other.car_coordinates[0] + 1)
            car.speed = 0

    def check_end_of_lap(self, car):
        car.car_coordinates = (car.car_coordinates %
                               self.length)

    def set_tail_distance(self, car, other):
        if car.car_coordinates[-1] >= other.car_coordinates[0]:
            return ((self.length + other.car_coordinates[0]) -
                    (car.car_coordinates[-1] + car.speed))
        return (other.car_coordinates[0] -
                (car.car_coordinates[-1] + car.speed))

    def simulate_n_seconds(self, n):
        speed_data = []
        position_data = []

        for _ in range(n):
            temp_list = []

            for index, car in enumerate(self.set_of_cars):

                td = self.set_tail_distance(car, self.set_of_cars[index-1])
                car.set_new_speed(self.set_of_cars[index-1], td)
                car.change_position()
                self.check_position(car, self.set_of_cars[index-1])
                self.check_end_of_lap(car)
                if index == 2:
                    print(index, car.car_coordinates, car.speed)

                if _ > n/2:
                    speed_data.append(car.speed)

                temp_list.append(car.car_coordinates)

            position_data.append(temp_list)

        return speed_data, position_data
