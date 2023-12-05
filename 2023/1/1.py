def parse_input(file):
    with open(file) as f:
        lines = [line for line in f.readlines()]
    return lines


def part1(lines):
    out = []
    for line in lines:
        line_num = [c for c in line if c.isnumeric()]
        if line_num:
            out += [int(str(line_num[0]) + str(line_num[-1]))]
    return sum(out)


def part2(lines):
    out = []
    numbers = {
        "one":      "1",
        "two":      "2",
        "three":    "3",
        "four":     "4",
        "five":     "5",
        "six":      "6",
        "seven":    "7",
        "eight":    "8",
        "nine":     "9"
    }
    for line in lines:
        out_line = []
        for idx in range(len(line)):
            if line[idx].isnumeric():
                out_line += line[idx]
                continue

            for key, val in numbers.items():
                if line.startswith(key, idx):
                    out_line += val
                    break

        out += [int(str(out_line[0]) + str(out_line[-1]))]
    return sum(out)


def main(file):
    lines = parse_input(file)
    return (f"Part 1: {part1(lines)}\n"
            f"Part 2: {part2(lines)}")


if __name__ == "__main__":
    print(main("input.txt"))
