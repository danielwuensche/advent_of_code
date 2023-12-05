class Monkey:
    def __init__(self, items: list, operation: list, test: int, if_true: str, if_false: str):
        self.items = items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.counter = 0

    def inspect(self, item: int):
        operation = self.operation[0]
        value = self.operation[1]
        value = item if value == "old" else int(value)
        match operation:
            case "+":
                return item + value
            case "*":
                return item * value

    def throw_item(self, idx: int):
        self.items.pop(idx)

    def catch_item(self, item: int):
        self.items.append(item)


def parse_input(_input: str) -> dict:
    with open(_input) as f:
        in_monkeys = f.read().split('\n\n')

    monkeys = {}
    for monkey in in_monkeys:
        name = items = operation = test = if_true = if_false = None
        for line in monkey.splitlines():
            line = line.split(':')
            match line[0]:
                case "  Starting items":
                    items = [int(i) for i in line[1].strip().split(', ')]
                case "  Operation":
                    operation = str(line[1].strip().split('new = old ')[1])
                    operation = operation.split()
                    operation = [operation[0], operation[1]]
                case "  Test":
                    test = int(line[1].strip().split('divisible by ')[1])
                case "    If true":
                    if_true = str(line[1].strip().split('throw to monkey')[1].strip())
                case "    If false":
                    if_false = str(line[1].strip().split('throw to monkey')[1].strip())
                case _:
                    name = str(line[0].strip('Monkey ')) if line[0].startswith('Monkey ') else None
        monkeys[name] = Monkey(items, operation, test, if_true, if_false)
    return monkeys


def start_round(monkeys: dict):
    for monkey in monkeys.keys():
        while monkeys[monkey].items:
            item = monkeys[monkey].items[0]

            # increase worry by operation
            item = monkeys[monkey].inspect(item)
            monkeys[monkey].counter += 1

            # relief
            item = int(item / 3)

            # test
            if item % monkeys[monkey].test == 0:
                # true, give to other monkey
                other_monkey = monkeys[monkey].if_true
            else:
                other_monkey = monkeys[monkey].if_false

            # throw item
            monkeys[monkey].throw_item(0)
            monkeys[other_monkey].catch_item(item)


def main(rounds: int):
    monkeys = parse_input('input.txt')

    _round = 0
    while _round < rounds:
        _round += 1
        start_round(monkeys)
#
    counters = [monkeys[monkey].counter for monkey in monkeys.keys()]
    counters = sorted(counters)[-2:]
    return counters[0] * counters[1]


if __name__ == "__main__":
    print(main(20))
