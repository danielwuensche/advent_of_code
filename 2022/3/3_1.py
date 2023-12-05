# uppercase -64 (65 - 90)
# lowercase -96 (97 - 122)
def main():
    with open('input.txt') as f:
        rucksacks = f.readlines()

    prio_sum = 0
    for r in rucksacks:
        if r:
            r = r.strip()
        else:
            continue

        # find shared item
        left = r[:int(len(r) / 2)]
        right = r[int(len(r) / 2):]
        for c in left:
            if c in right:
                item = c
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
