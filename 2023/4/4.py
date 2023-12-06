class Card:
    def __init__(self, num_winning: list, num_actual: list):
        self.instances = 1
        self.num_winning = num_winning
        self.num_actual = num_actual
        self.matches = self.match_winning_numbers(self.num_winning, self.num_actual)

    @staticmethod
    def match_winning_numbers(winning: list, actual: list):
        matches = 0
        for n in actual:
            if n in winning:
                matches += 1
        return matches


def parse_input(file):
    with open(file) as f:
        cards = {}
        for card in f.readlines():
            card = card.split(': ')
            card[1] = card[1].split(' | ')
            for idx, l in enumerate(card[1]):
                card[1][idx] = l.strip().split()
            cards[card[0].split()[1]] = Card(num_winning=card[1][0], num_actual=card[1][1])
    return cards


def part1(cards):
    points = []
    for card in cards:
        matches = cards[card].matches
        card_points = pow(2, matches-1) if matches > 0 else 0
        points += [card_points]
    return sum(points)


def part2(cards):
    total = 0
    for card in cards:
        for _ in range(cards[card].instances):
            matches = cards[card].matches
            for next_card in range(int(card)+1, int(card)+1+matches):
                next_card = str(next_card)
                if str(next_card) in cards.keys():
                    cards[next_card].instances += 1
        total += cards[card].instances
    return total


def main(file):
    cards = parse_input(file)
    return (f"Part 1: {part1(cards)}\n"
            f"Part 2: {part2(cards)}")


if __name__ == "__main__":
    print(main("input.txt"))
