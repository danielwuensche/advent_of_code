def part1(lines):
    p1_count = 0
    idx_lines = -1
    for line in lines:
        idx_lines += 1
        # if first or last line
        if idx_lines == 0 or idx_lines == len(lines)-1:
            p1_count += len(line)
            continue
        # all the other lines
        idx_line = -1
        for c in line:
            visible = True
            c = int(c)
            idx_line += 1
            # if first or last character
            if idx_line == 0 or idx_line == len(line)-1:
                p1_count += 1
                continue
            # all the other characters
            # get other horizontal trees
            horizontal_left = [int(line[n]) for n in range(idx_line)]
            horizontal_right = [int(line[n]) for n in range(idx_line+1, len(line))]
            vertical_up = [int(lines[n][idx_line]) for n in range(idx_lines)]
            vertical_down = [int(lines[n][idx_line]) for n in range(idx_lines+1, len(lines))]
            for o in horizontal_left:
                if o >= c:
                    visible = False
                    break
                visible = True
            if not visible:
                for o in horizontal_right:
                    if o >= c:
                        visible = False
                        break
                    visible = True
            if not visible:
                for o in vertical_up:
                    if o >= c:
                        visible = False
                        break
                    visible = True
            if not visible:
                for o in vertical_down:
                    if o >= c:
                        visible = False
                        break
                    visible = True

            if visible:
                p1_count += 1
    return p1_count


def part2(lines):
    scores = []

    idx_lines = -1
    for line in lines:
        idx_lines += 1

        # if trees are on the edge, scenic score will be 0
        if idx_lines == 0 or idx_lines == len(lines) - 1:
            continue

        idx_line = -1
        for c in line:
            visible = True
            c = int(c)
            idx_line += 1

            # if the tree is on the edge, scenic score will be 0
            if idx_line == 0 or idx_line == len(line)-1:
                continue

            score = 1

            horizontal_left = [int(line[n]) for n in range(idx_line)][::-1]
            distance = 0
            for o in horizontal_left:
                distance += 1
                if o >= c:
                    break
            score *= distance

            horizontal_right = [int(line[n]) for n in range(idx_line+1, len(line))]
            distance = 0

            for o in horizontal_right:
                distance += 1
                if o >= c:
                    break
            score *= distance

            vertical_up = [int(lines[n][idx_line]) for n in range(idx_lines)][::-1]
            distance = 0
            for o in vertical_up:
                distance += 1
                if o >= c:
                    break
            score *= distance

            vertical_down = [int(lines[n][idx_line]) for n in range(idx_lines+1, len(lines))]
            distance = 0
            for o in vertical_down:
                distance += 1
                if o >= c:
                    break
            score *= distance

            scores += [[idx_lines, idx_line, score]]

    scores.sort(key=lambda n: n[2], reverse=True)
    return scores[0][2]


def main(file):
    with open(file) as f:
        lines = [line.strip() for line in f.readlines()]

    p1 = part1(lines)
    p2 = part2(lines)

    return p1, p2


if __name__ == "__main__":
    # f = "input_example_p1.txt"
    f = "input.txt"
    print(main(f))
