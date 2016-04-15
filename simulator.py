import numpy as np
from road import Road


def main():

    road = Road(number_of_cars=30)
    road.place_cars()

    speed_limits = []

    for _ in range(100):
        speeds, positions = road.simulate_n_seconds(60)

        speed_limit = np.mean(speeds) + np.std(speeds)
        speed_limits.append(speed_limit)

    print(int(np.mean(speed_limits)))
    return int(np.mean(speed_limits))


if __name__ == '__main__':
    main()
