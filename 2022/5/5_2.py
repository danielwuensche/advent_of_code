def get_stacks(_in: list):
    stacks = {}
    for line in _in:
        if line[1] == "1":
            break
        for i in range(1, len(line), 4):
            idx = i // 4 + 1    # stack number
            if idx in stacks.keys():
                stacks[idx] += line[i]
            else:
                stacks[idx] = line[i]
    # reverse and strip
    for i in stacks.keys():
        stacks[i] = stacks[i][::-1].strip()

    return stacks


def get_commands(_in: list):
    for line in _in:
        line = line.split()
        _move_amount, _from_stack, _to_stack = map(int, [line[1], line[3], line[5]])





def main():
    with open('input.txt') as f:
        lines = f.readlines()

    stacks = get_stacks(lines[:lines.index('\n')])
    commands = lines[lines.index('\n')+1:]

    for comm in commands:
        comm = comm.split()
        move_amount, from_stack, to_stack = map(int, [comm[1], comm[3], comm[5]])
        crates_to_move = stacks[from_stack][-move_amount:]
        stacks[from_stack] = stacks[from_stack][:-move_amount]
        stacks[to_stack] += crates_to_move

    _out = ''
    for key in stacks.keys():
        _out += stacks[key][-1]

    return _out



if __name__ == "__main__":
    print(main())