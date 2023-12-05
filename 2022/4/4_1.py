def main():
    # read input
    with open('input.txt') as f:
        pairs = f.readlines()

    counter = 0
    for pair in pairs:
        # split pair and split range
        pair = pair.strip().split(',')
        r1 = pair[0].split('-')
        r1 = [int(r1[0]), int(r1[1])]
        r2 = pair[1].split('-')
        r2 = [int(r2[0]), int(r2[1])]
        if (r1[0] >= r2[0] and r1[1] <= r2[1]) or (r2[0] >= r1[0] and r2[1] <= r1[1]):
            counter += 1
    return counter


if __name__ == "__main__":
    print(main())
