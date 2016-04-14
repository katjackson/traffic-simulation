from car import Car

class Road():

    def __init__(self, length_of_road=1000, number_of_cars=5):
        self.number_of_cars = int(number_of_cars)
        self.length = int(length_of_road)
        self.set_of_cars = []

    def place_cars(self):
        interval = round(self.length / (self.number_of_cars + 1))
        for number in range(number_of_cars):
            self.set_of_cars.append(Car(number * interval))

        
