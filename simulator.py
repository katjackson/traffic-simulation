import numpy as np
from car import Road

def main():

    road = Road(number_of_cars=30)
    road.place_cars()

    speed_limits = []
    positions_list = []
    iteration_number = 2
    for _ in range(iteration_number):
        speeds, positions = road.simulate_n_seconds(60)

        speed_limit = np.mean(speeds) + np.std(speeds)
        speed_limits.append(speed_limit)

        if _ > iteration_number - 3:
            positions_list.append(positions)

    for iteration in positions_list:
        print(iteration)
    print(int(np.mean(speed_limits)))
    return int(np.mean(speed_limits))


if __name__ == '__main__':
    main()
