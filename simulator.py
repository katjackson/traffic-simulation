from road import Road


def main():

    road = Road(number_of_cars=30)
    road.place_cars()

    total_data = []

    for _ in range(60):
        temp_data = []
        number = 0
        for index, car in enumerate(road.set_of_cars):
            print('idx:', index)
            if index == 29:
                number = 0
            else:
                number = index + 1
            print('numb:', number)
            print('car:', road.set_of_cars[index].speed)
            print('nextcar:', road.set_of_cars[number].speed)
            car.choose_speed_change(road.set_of_cars[number])

            car.change_position()
            temp_data.append(car.speed)
        total_data.append(temp_data)
    print(total_data[40:55])

if __name__ == '__main__':
    main()
