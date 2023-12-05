def draw(cycle: int, x: int):
    pos = (cycle - 1) % 40
    return "#" if pos in [x - 1, x, x + 1] else '.'


def main():
    with open('input.txt') as f:
        lines = f.readlines()

    crt = ""
    cycle = 0
    x = 1

    for line in lines:
        line = line.split()
        instr = line[0]
        val = int(line[1]) if len(line) > 1 else None

        cycle += 1

        if instr == "noop":
            crt += draw(cycle, x)

        if instr == "addx":
            crt += draw(cycle, x)

            cycle += 1

            crt += draw(cycle, x)
            x += val

    frame = ""
    for i in range(0, len(crt), 40):
        frame += crt[i:i+39] + '\n'

    return frame


if __name__ == "__main__":
    print(main())
