with open('input.txt') as f:
    lines = [[l.strip() for l in line.split()] for line in f.readlines()]

fs = []
sizes = {}
current_dir = []
for line in lines:
    if line[0] == '$':
        # command
        if line[1] == 'cd':
            if line[2] == '..':
                if len(current_dir) > 1:
                    current_dir.pop(-1)
            elif line[2] == '/':
                current_dir = []
            else:
                current_dir.append(line[2])
    else:
        # no command, ls output
        if line[0] == "dir":
            continue
        else:
            path = '/'.join(current_dir)
            size = int(line[0])

            for i in sizes.keys():
                if i in path:
                    sizes[i] += size

            if path not in sizes.keys():
                sizes[path] = size

# for i in sizes.keys():
#     print(sizes[i], i)

for i in sizes.values():
    if i <= 100000:
        print(i)

print(sum([i for i in sizes.values() if i <= 100000]))
