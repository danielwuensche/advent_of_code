import time
import itertools

# start = time.process_time()
# print(time.process_time() - start)

class Sensor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.scan_range = None
        self.bounds = None      # (_ymin, _ymax, _xmin, _xmax)


def parse_input(file):
    with open(file) as f:
        lines = f.readlines()

    sensors = []
    beacons = []
    for line in lines:
        line_sensor = line.split(':')[0]
        sensor_x = int(line_sensor.split('x=')[1].split(',')[0])
        sensor_y = int(line_sensor.split('y=')[1].split(',')[0])
        s = Sensor(sensor_x, sensor_y)

        line_beacon = line.split(':')[1]
        beacon_x = int(line_beacon.split('x=')[1].split(',')[0])
        beacon_y = int(line_beacon.split('y=')[1].split(',')[0])
        b = [(beacon_x, beacon_y)]

        _range = abs(s.x - b[0][0]) + abs(s.y - b[0][1])
        _ymax = s.y + _range
        _ymin = s.y - _range
        _xmax = s.x + _range
        _xmin = s.x - _range

        s.scan_range = _range
        s.bounds = (_ymin, _ymax, _xmin, _xmax)

        sensors.append(s)
        beacons.append(b)

    return sensors, beacons


def part1(sensors, beacons, y_target):
    x_coords = set()
    for s in sensors:
        if not s.bounds[0] <= y_target <= s.bounds[1]:
            continue
        y_distance = abs(s.y - y_target)
        x_range = set(range(s.bounds[2] + y_distance, s.bounds[3] - y_distance + 1))
        x_coords.update(x_range if x_range else {s.x})

    for b in filter(lambda x: x[0][1] == y_target and x[0][0] in x_coords, beacons):
        x_coords.remove(b[0][0])

    return len(x_coords)


def part2(sensors, search_space):
    # gather sensor ranges
    ranges = {}
    for s in sensors:
        for y in [i for i in range(s.bounds[0], s.bounds[1]+1) if 0 <= i <= search_space]:
            y_distance = abs(s.y - y)
            x_min = s.bounds[2] + y_distance
            x_min = 0 if x_min < 0 else x_min

            x_max = s.bounds[3] - y_distance
            x_max = search_space if x_max > search_space else x_max
            if y in ranges.keys():
                ranges[y] += [(x_min, x_max)]
            else:
                ranges[y] = [(x_min, x_max)]

    point = None
    for y in ranges.keys():
        ranges[y].sort(key=lambda n: (n[0], n[1]))
        new = []
        current_range = ()
        for i in range(len(ranges[y])):
            if i + 1 < len(ranges[y]):
                if not current_range:
                    current_range = ranges[y][i]
                _next = ranges[y][i + 1]

                # if next low is lower than old high, same range
                # if next low is only one higher than old high, same range
                if _next[0] <= current_range[1] + 1:
                    new_low = current_range[0]
                    new_high = _next[1] if _next[1] > current_range[1] else current_range[1]
                    current_range = (new_low, new_high)
                    continue
            if current_range not in new:
                new += [current_range]
                current_range = ()

        if len(new) > 1:
            point = (new[0][1] + 1, y)
            break
    p2 = point[0] * 4000000 + point[1] if point is not None else point
    return p2


def main(file, p1_target, p2_search_space):
    _input = parse_input(file)
    sensors, beacons = map(list, _input)

    p1 = part1(sensors, beacons, p1_target)

    start = time.process_time()
    p2 = part2(sensors, p2_search_space)
    print(time.process_time() - start)

    return p1, p2


if __name__ == "__main__":
    # print(main("input_example.txt", 10, 20))
    print(main("input.txt", 2000000, 4000000))
