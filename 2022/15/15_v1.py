import time


class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    __radd__ = __add__

    def __sub__(self, other):
        return Position(self.x - other.x, self.y - other.y)

    __rsub__ = __sub__

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __str__(self):
        return f"Position({self.x}, {self.y})"

    __repr__ = __str__

    def __eq__(self, other) -> bool:
        return True if self.x == other.x and self.y == other.y else False

    def distance(self, other):
        return max(self.x, other.x) - min(self.x, other.x) + max(self.y, other.y) - min(self.y, other.y)


class Sensor(Position):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)


class Beacon(Position):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)


def parse_input(file):
    with open(file) as f:
        lines = f.readlines()

    sensors = []
    beacons = []
    for line in lines:
        line_sensor = line.split(':')[0]
        sensor_x = int(line_sensor.split('x=')[1].split(',')[0])
        sensor_y = int(line_sensor.split('y=')[1].split(',')[0])
        sensors.append(Sensor(sensor_x, sensor_y))

        line_beacon = line.split(':')[1]
        beacon_x = int(line_beacon.split('x=')[1].split(',')[0])
        beacon_y = int(line_beacon.split('y=')[1].split(',')[0])
        beacons.append(Beacon(beacon_x, beacon_y))

    return sensors, beacons


def part1(beacons, sensors, y_target):
    # part 1
    x_coords = []
    for s, b in zip(sensors, beacons):
        s.radius = s.distance(b)
        # if target y is not in the range of this sensor, the sensor is irrelevant
        if not (s.y - s.radius) <= y_target <= (s.y + s.radius):
            continue
        # sensors y distance to target y
        y_distance = max(s.y, y_target) - min(s.y, y_target)
        # remaining radius to walk on the x axis
        x_distance = s.radius - y_distance
        x_range = [x for x in range((s.x - x_distance), (s.x + x_distance + 1))]
        if x_range:
            x_coords += x_range
        else:
            x_coords.append(s.x)
        x_coords = list(set(x_coords))
    for b in beacons:
        if b.y == y_target and b.x in x_coords:
            x_coords.pop(x_coords.index(b.x))
    p1 = len(set(x_coords))
    return p1


def part2(sensors, search_space):
    for s in sensors:
        s.sensor_range = []
        for y in [i for i in range(s.y - s.radius, s.y + s.radius + 1) if 0 <= i <= search_space]:
            y_distance = max(s.y, y) - min(s.y, y)
            x_distance = s.radius - y_distance

            x_min = s.x - x_distance
            x_min = 0 if x_min < 0 else x_min

            x_max = s.x + x_distance
            x_max = search_space if x_max > search_space else x_max
            s.sensor_range.append([(x_min, x_max), y])
    ranges = [[r[0], r[1]] for s in sensors for r in s.sensor_range]
    # # sort x ranges by lowest
    ranges.sort(key=lambda n: n[1])
    dict_ranges = {}
    for r in ranges:
        y = r[1]
        x = r[0]
        if y in dict_ranges.keys():
            dict_ranges[y] += [x]
        else:
            dict_ranges[y] = [x]
    point = None
    combined_ranges = {}
    for y in dict_ranges.keys():
        dict_ranges[y].sort(key=lambda n: (n[0], n[1]))
        new = []
        current_range = ()
        for i in range(len(dict_ranges[y])):
            if i + 1 < len(dict_ranges[y]):
                if not current_range:
                    current_range = dict_ranges[y][i]
                _next = dict_ranges[y][i + 1]

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

        combined_ranges[y] = new
        if len(combined_ranges[y]) > 1:
            point = (combined_ranges[y][0][1] + 1, y)
            break
    p2 = point[0] * 4000000 + point[1] if point is not None else point
    return p2


def main(file, y_target, search_space):
    _input = parse_input(file)
    sensors, beacons = map(list, _input)

    p1 = part1(beacons, sensors, y_target)

    # part 2

    start = time.process_time()
    p2 = part2(sensors, search_space)
    elapsed = (time.process_time() - start)
    print(elapsed)

    return p1, p2


# print(main('input_example_p1.txt', 10, 20)) # = 6425133
print(main('input.txt', 2000000, 4000000))



