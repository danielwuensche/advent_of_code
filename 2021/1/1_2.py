def main():
    with open('input.txt') as f:
        depths = f.readlines()
        newdepths = []
        for i in depths:
            newdepths += [int(i)]
        depths = newdepths

    window = []
    while len(depths) >= 3:
        window += [sum(depths[:3])]
        depths = depths[1:]

    counter = 0
    for i in range(1, len(window)):
        if int(window[i]) > int(window[i-1]):
            counter += 1
    # prev = None
    # for d in depths:
    #     d = d.strip()
    #     if prev and d != '' and d > prev:
    #         counter += 1
    #     print(counter, d, prev)
    #     prev = d
    return counter


if __name__ == "__main__":
    print(main())
