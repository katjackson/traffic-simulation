import numpy as np
from road import Road


def main():
    road = Road(number_of_cars=30)
    number_of_runs = 100
    seconds_in_run = 60

    road.place_cars()
    speed_limit_list = []
    positions_list = []
    speeds_list = []

    for _ in range(number_of_runs):
        speeds, positions = road.simulate_n_seconds(seconds_in_run)

        speed_limit_list.append(np.mean(speeds) + np.std(speeds))

        if _ in {0, 10, 35, 75, 99}:
            positions_list.append(positions[:])
            speeds_list.append(speeds)

    return int(np.mean(speed_limit_list)), positions_list, speeds_list

if __name__ == '__main__':
    main()
