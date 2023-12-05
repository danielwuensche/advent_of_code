from ast import literal_eval
from functools import cmp_to_key

with open('input.txt') as f:
    # split input on empty line, get list of packet pairs
    pairs = [[literal_eval(line) for line in pair.splitlines()] for pair in f.read().split('\n\n')]


def compare(a, b) -> bool | None:
    # convert input to lists
    if not isinstance(a, list):
        a = [a]
    if not isinstance(b, list):
        b = [b]

    # go through lists
    for x, y in zip(a, b):
        # element is list
        if isinstance(x, list) or isinstance(y, list):
            result = compare(x, y)
        else:
            result = 0 if x == y else y - x

        if result != 0:
            return result

    return 0 if len(a) == len(b) else len(b) - len(a)


def part1(pairs):
    correct = []
    idx = 0
    for pair in pairs:
        idx += 1
        a, b = map(list, [pair[0], pair[1]])
        result = compare(a, b)
        if result:
            correct.append(idx)

    return sum(correct)


def part2(pairs):
    sorted_list = sorted([packet for pair in pairs for packet in pair] + [[[2]], [[6]]],
                         key=cmp_to_key(compare), reverse=True)
    result = 1
    for i, item in enumerate(sorted_list, 1):
        if item in [[[2]], [[6]]]:
            result *= i

    return result

print(part1(pairs))
print(part2(pairs))