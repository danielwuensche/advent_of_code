class Dir:
    def __init__(self, name: str, parent, isfile=False, size=0):
        self.name = name
        self.parent = parent
        self.isfile = isfile
        self.size = size
        if not self.isfile:
            self.content = []

    def __str__(self):
        return f"Directory: {self.name}, size: {self.size}, children: {len(self.content)}\n"

    __repr__ = __str__


def generate_tree(lines):
    tree = Dir("/", None)
    current_dir = tree
    for line in lines:
        if line[0] == '$':
            # command
            if line[1] == 'cd':
                if line[2] == '..':
                    if current_dir.name != "/":
                        current_dir = current_dir.parent
                elif line[2] == '/':
                    current_dir = tree
                else:
                    found = False
                    for c in current_dir.content:
                        if c.name == line[2]:
                            current_dir = c
                            found = True
                            break
                    if not found:
                        current_dir.content.append(Dir(line[2], current_dir))
        else:
            # no command, ls output
            name = line[1]
            if line[0] == "dir":
                current_dir.content.append(Dir(name, current_dir))
            else:
                size = int(line[0])
                found = False
                for c in current_dir.content:
                    if c.name == name:
                        c.size = size
                        found = True
                if not found:
                    current_dir.content.append(Dir(name, current_dir, True, size))
    return tree


def calculate_dir_sizes(directory) -> None:
    new_size = 0
    if directory.isfile:
        print("not a directory")
        return
    for c in directory.content:
        if not c.isfile:
            calculate_dir_sizes(c)
        new_size += c.size
    directory.size = new_size


def part1(directory):
    size = 0
    if directory.size <= 100000:
        size += directory.size
    for c in directory.content:
        if c.isfile:
            continue
        else:
            size += part1(c)
    return size


def part2(directory, min_size):
    candidates = []
    if directory.size >= min_size:
        candidates += [directory]
        for c in directory.content:
            if not c.isfile:
                candid = part2(c, min_size)
                if candid is not None:
                    candidates += [candid]
    candidates.sort(key=lambda n: n.size)
    return candidates[0] if candidates else None


def main(filename):
    with open(filename) as f:
        lines = [[l.strip() for l in line.split()] for line in f.readlines()]

    tree = generate_tree(lines)
    calculate_dir_sizes(tree)

    print(part1(tree))

    disk_total = 70000000
    disk_used = disk_total - tree.size
    disk_needed = 30000000
    disk_free_needed = disk_needed - disk_used

    print(part2(tree, disk_free_needed))

    breakpoint()




if __name__ == "__main__":
    # print(main('input_example_p1.txt'))
    print(main('input.txt'))
