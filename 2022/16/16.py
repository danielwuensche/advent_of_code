class Valve:
    def __init__(self, name, rate, opened, tunnels):
        self.name = name
        self.rate = rate
        self.opened = opened
        self.tunnels = tunnels

    def __str__(self):
        return self.name

    __repr__ = __str__


def parse_input(file):
    with open(file) as f:
        lines = [line.split() for line in f.readlines()]
    valves = {}
    for line in lines:
        name = line[1]
        rate = int(line[4].split('=')[1][:-1])
        opened = False
        tunnels = [tunnel.strip(',') for tunnel in line[9:]]
        valves[name] = Valve(name, rate, opened, tunnels)
    # replace tunnel names with corresponding valve objects
    for valve in valves.keys():
        valves[valve].tunnels = sorted([valves[t] for t in valves[valve].tunnels], key=lambda n: n.rate, reverse=True)
    return valves


def where_to_go(to_go, to_open):
    chosen = False
    for i in [j for j in to_go if j in to_open]:
        if i in to_open:
            chosen = i
            break
    if not chosen:
        for i in [j for j in to_go if j not in to_open]:
            chosen = where_to_go(i.tunnels, to_open)
            if chosen:
                break
    return chosen


def main(file):
    valves = parse_input(file)
    pressure = 0
    limit = 30
    timer = 0
    location = None
    valves_opened = []
    to_open = []
    for i in valves.keys():
        if not location:
            location = valves[i]
        if valves[i].rate != 0:
            to_open += [valves[i]]

    while timer <= limit:
        timer += 1
        if valves_opened:
            _pressure_to_add = sum([valve.rate for valve in valves_opened])
            pressure += _pressure_to_add
            print(f'adding {_pressure_to_add} pressure, now {pressure}')
        # open valve if rate is not 0
        if location in to_open:
            # open valve
            location.opened = True
            print(f'opening {location} with flow rate {location.rate}, left to open: {to_open}')
            valves_opened += [location]
            to_open.pop(to_open.index(location))
            continue
        if not to_open:
            continue
        # check where to go next
        to_go = [tunnel for tunnel in location.tunnels]
        chosen = where_to_go(to_go, to_open)
        if chosen:
            location = chosen
            print(f'going to {location} (options: {to_go})')

    return pressure



if __name__ == "__main__":
    print(main("input_example.txt"))
    # print(main("input.txt"))
