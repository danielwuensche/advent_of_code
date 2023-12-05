# uppercase -64 (65 - 90)
# lowercase -96 (97 - 122)
def main():
    with open('input.txt') as f:
        rucksacks = f.readlines()

    groups = []
    while rucksacks:
        groups += [rucksacks[:3]]
        rucksacks = rucksacks[3:]

    prio_sum = 0
    for a, b, c in groups:
        if a:
            a = a.strip()
        if b:
            b = b.strip()
        if c:
            c = c.strip()

        # find shared item
        for i in a:
            if i in b and i in c:
                item = i
                break

        # prio of shared item
        if 97 <= ord(item) <= 122:
            # lowercase prio from 1 through 26
            prio = ord(item) - 96
        elif 65 <= ord(item) <= 90:
            # uppercase prio from 27 through 52
            prio = ord(item) - 64 + 26

        # add prio to sum
        prio_sum += prio
    return prio_sum


if __name__ == "__main__":
    print(main())
