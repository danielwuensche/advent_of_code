def rps(opponent: int, me: int):
    score = 0
    if me - opponent == 1 or (me == 1 and opponent == 3):
        score += me + 6
    elif opponent - me == 0:
        score += me + 3
    else:
        score += me
    return score


def part1(lines):
    score = opponent = me = 0
    for line in lines:
        if line[0] == "A":
            opponent = 1
        elif line[0] == "B":
            opponent = 2
        elif line[0] == "C":
            opponent = 3
        if line[1] == "X":
            me = 1
        elif line[1] == "Y":
            me = 2
        elif line[1] == "Z":
            me = 3
        score += rps(opponent, me)
    return score


def part2(lines):
    score = opponent = me = 0
    for line in lines:
        if line[0] == "A":
            opponent = 1
        elif line[0] == "B":
            opponent = 2
        elif line[0] == "C":
            opponent = 3
        if line[1] == "X":
            me = 3 if opponent == 1 else opponent - 1
        elif line[1] == "Y":
            me = opponent
        elif line[1] == "Z":
            me = 1 if opponent == 3 else opponent + 1
        score += rps(opponent, me)
    return score


def main():
    with open("input.txt") as f:
        lines = [line.split() for line in f.readlines()]
    p1 = part1(lines)
    p2 = part2(lines)
    return p1, p2


if __name__ == "__main__":
    print(main())
