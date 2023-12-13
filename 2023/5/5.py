
class Item:
    def __init__(self, category: str, value: int):
        self.category = category
        self.value = value


def parse_input(file):
    seeds = []
    maps = {}
    current_map = ""
    with open(file) as f:
        for line in f.readlines():

            if line.startswith("seeds: "):
                seeds += [int(seed) for seed in line.split(": ")[1].split()]
                continue

            if line.endswith(" map:\n"):
                current_map = line.removesuffix(" map:\n")
                continue

            if line[0].isnumeric():
                if current_map not in maps.keys():
                    maps[current_map] = []
                line = line.split()
                dst_start = int(line[0])
                src_start = int(line[1])
                range_len = int(line[2])

                maps[current_map] += [{"dst_start": dst_start,
                                      "src_start": src_start,
                                      "range": range_len}]
                continue

    return {"seeds": seeds, "maps": maps}


def calculate_location(seed: Item, maps: dict):
    while seed.category != "location":

        # find map which has the current category as source
        map_needed = ""
        while not map_needed:
            for cmap in maps.keys():
                if cmap.startswith(seed.category):
                    map_needed = cmap
                    break

        # find relevant range and get destination value
        dst_value = None
        for crange in maps[map_needed]:
            # get destination value
            if seed.value in range(crange["src_start"],
                                   crange["src_start"] + crange["range"]):
                distance = seed.value - crange["src_start"]
                dst_value = crange["dst_start"] + distance
                break

        # get destination category
        dst_category = map_needed.split("-to-")[1]

        seed.value = dst_value if dst_value else seed.value
        seed.category = dst_category

    return seed


def part1(_seeds: list, maps: dict):
    seeds = [Item("seed", seed) for seed in _seeds]
    for seed in seeds:
        seed = calculate_location(seed, maps)
    return sorted(seeds, key=lambda x: x.value)[0].value


def part2(_seeds: list, maps: dict):
    # span = 2
    # _seeds = [str(seed) for seed in _seeds]
    # print([" ".join(_seeds[i:i+span]) for i in range(0, len(_seeds), span)])
    seeds = []
    while _seeds:
        seeds += [range(_seeds[0], _seeds[0]+_seeds[1])]
        _seeds = _seeds[2:]

    # seeds = [Item("seed", seed) for srange in seeds for seed in srange]
    r = 0
    i = 0
    lowest = None
    for srange in seeds:
        r += 1
        print(f"range {r}")
        for seed in srange:
            i += 1
            if i % 10000000 == 0:
                print(i)
            seed = Item("seed", seed)
            seed = calculate_location(seed, maps)
            if not lowest or seed.value < lowest:
                lowest = seed.value
                print(f"lowest: {lowest}")
    return sorted(seeds, key=lambda x: x.value)[0].value


def main(file):
    _input = parse_input(file)
    seeds = _input["seeds"]
    maps = _input["maps"]
    return (f"Part 1: {part1(seeds, maps)}\n"
            f"Part 2: {part2(seeds, maps)}")


if __name__ == "__main__":
    print(main("input.txt"))
