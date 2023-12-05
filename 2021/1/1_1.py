def main():
    with open('input.txt') as f:
        depths = f.read()
        depths = depths.split('\n')

    counter = 0
    for i in range(1, len(depths)):
        if int(depths[i]) > int(depths[i-1]):
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
