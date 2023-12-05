def main():
    with open("input.txt") as f:
        elves = [elf.splitlines() for elf in f.read().split('\n\n')]
        sums = []
        for elf in elves:
            cal = 0
            for food in elf:
                cal += int(food)
            sums += [cal]
    p1 = sorted(sums, reverse=True)[0]
    p2 = sum(sorted(sums, reverse=True)[:3])
    return p1, p2

if __name__ == "__main__":
    print(main())