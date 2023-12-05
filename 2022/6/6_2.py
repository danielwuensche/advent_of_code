def main():
    with open('input.txt') as f:
        line = f.read()

    for i in range(13, len(line)):
        _set = set(line[i-13:i+1])
        if len(_set) == 14:
            return i+1


if __name__ == '__main__':
    print(main())
