def parse_input(file):
    with open(file) as f:
        games = {}
        for line in f.readlines():
            game = line.split(':')[0].split()[-1]
            game = int(game)
            rounds = []
            for r in line.split(':')[1].split(';'):

                red = 0
                green = 0
                blue = 0
                for color in r.split(','):
                    color = color.split()
                    match color[-1]:
                        case 'red':
                            red = color[0]
                        case 'green':
                            green = color[0]
                        case 'blue':
                            blue = color[0]
                rounds += [{
                    'red': int(red),
                    'green': int(green),
                    'blue': int(blue)
                }]
            games[game] = rounds
    return games


def part1(games):
    games_possible = []
    max_red = 12
    max_green = 13
    max_blue = 14
    for game in games.keys():
        game_possible = True
        for r in games[game]:
            if r['red'] > max_red:
                game_possible = False
                break
            if r['green'] > max_green:
                game_possible = False
                break
            if r['blue'] > max_blue:
                game_possible = False
                break
        if game_possible:
            games_possible += [game]
    return sum(games_possible)


def part2(games):
    power = 0
    for game in games.keys():
        min_red = 0
        min_green = 0
        min_blue = 0
        for r in games[game]:
            if r['red'] > min_red:
                min_red = r['red']
            if r['green'] > min_green:
                min_green = r['green']
            if r['blue'] > min_blue:
                min_blue = r['blue']
        power += min_red * min_green * min_blue
    return power


def main(file):
    games = parse_input(file)
    return (f"Part 1: {part1(games)}\n"
            f"Part 2: {part2(games)}")


if __name__ == "__main__":
    print(main("input.txt"))
