import json


def throw_error():
    breakpoint()


def parse_out(out):
    out = out.split()
    a = int(out[0])
    b = int(out[2])
    if not a < b:
        print(f'{a} < {b} is wrong')


def compare(a, b):
    # check if both are integers
    if type(a) == int and type(b) == int:
        # a should be smaller than b
        if a < b:
            out = f'{a} < {b}'
            parse_out(out)
            return "yes"
        # if a is greater than b, wrong order
        elif a > b:
            out = f'{b} < {a}'
            parse_out(out)
            return "no"
    # check if both are lists
    elif type(a) == list and type(b) == list:
        # if a is empty and b is not, right order
        if len(a) == 0 and len(b) > 0:
            # out = f'a ({len(a)}) is empty and b ({len(b)}) is not'
            out = f'{len(a)} < {len(b)}'
            parse_out(out)
            return "yes"
        # if b is empty and a is not, wrong order
        elif len(a) > 0 and len(b) == 0:
            # out = f'b ({len(b)}) is empty and a ({len(a)}) is not'
            out = f'{len(b)} < {len(a)}'
            parse_out(out)
            return "no"
        # if both lists are populated
        elif len(a) != 0 and len(b) != 0:
            # compare the list items
            for i in range(0, len(a)):
                comp = compare(a[i], b[i])
                # if result is yes, right order
                if comp == "yes":
                    return "yes"
                # if result is no, wrong order
                elif comp == "no":
                    return "no"
                # if a is shorter than b, right order
                elif len(a) < len(b):
                    # out = f'a ({len(a)}) is shorter than b ({len(b)})'
                    out = f'{len(a)} < {len(b)}'
                    parse_out(out)
                    return "yes"
                # if a is longer than b, wrong order
                elif len(a) > len(b):
                    # out = f'b ({len(b)}) is shorter than a ({len(a)})'
                    out = f'{len(b)} < {len(a)}'
                    parse_out(out)
                    return "no"
    # if one is a list and the other an integer, convert integer to list
    elif (type(a) == list and type(b) == int) or (type(a) == int and type(b) == list):
        if type(a) == int:
            a = [a]
        else:
            b = [b]
        return compare(a, b)
    return "unknown"


def main():
    correct = []
    with open('input.txt') as f:
        # split input on empty line, get list of packet pairs
        lines = [line.splitlines() for line in f.read().split('\n\n')]

    for line in lines:
        # convert packet strings to python list objects
        original_line = line
        line = [json.loads(l) for l in line]

        # map packet pair, a contains left packet, b contains right packet
        a, b = map(list, [line[0], line[1]])

        # compare list elements of a and b
        # if result is yes, add index (starting at 1) to list of packets in correct order
        if compare(a, b) == "yes":
            idx = lines.index(original_line)+1
            correct.append(idx)

    return sum(correct), len(correct), len(lines)


if __name__ == "__main__":
    print(main())
    # correct = 6068
