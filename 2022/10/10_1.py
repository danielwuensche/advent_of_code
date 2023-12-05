def main():
    with open('input.txt') as f:
        lines = f.readlines()

    interesting = [20, 60, 100, 140, 180, 220]
    result = [[0, 1]]
    cycle = 0
    x = 1

    for line in lines:
        line = line.split()
        instr = line[0]
        val = int(line[1]) if len(line) > 1 else None

        cycle += 1

        if instr == "noop":
            result.append([cycle, x])
        if instr == "addx":
            result.append([cycle, x])
            cycle += 1
            result.append([cycle, x])
            x += val

    return sum([r[1] * r[0] for r in result if r[0] in interesting])


if __name__ == "__main__":
    print(main())
