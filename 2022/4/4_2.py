def main():
    # read input
    with open('input.txt') as f:
        pairs = f.readlines()

    counter = 0
    for pair in pairs:
        # split pair and split range
        pair = pair.strip().split(',')
        r1 = pair[0].split('-')
        r2 = pair[1].split('-')
        r1r = range(int(r1[0]), int(r1[1])+1)
        r2r = range(int(r2[0]), int(r2[1])+1)

        # speed optimization
        if len(r1r) > len(r2r):
            _t = r1r
            r1r = r2r
            r2r = _t

        for a in r1r:
            if a in r2r:
                counter += 1
                # print(f'{a} in {r2r}')
                break
            # print(f'{a} not in {r2r}')
    return counter


if __name__ == "__main__":
    print(main())
