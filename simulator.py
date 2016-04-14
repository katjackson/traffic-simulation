from road import Road


def main():

    road = Road(number_of_cars=30)
    road.place_cars()

    total_data = []
    print(road.set_of_cars[0].speed)
    road.set_of_cars[0].choose_speed_change(road.set_of_cars[1])
    print(road.set_of_cars[0].speed)
    for _ in range(60):
        temp_data = []
        number = 0
        for index, car in enumerate(road.set_of_cars):
            if index == 29:
                number = 0
            else:
                number = index + 1
            car.choose_speed_change(road.set_of_cars[number])

            car.change_position()
            temp_data.append(car.speed)
        total_data.append(temp_data)
    print(total_data[2:8])

if __name__ == '__main__':
    main()
