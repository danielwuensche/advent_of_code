from Knot import Knot
from matplotlib import pyplot as plt


def main(filename, knot_amount):
    with open(filename) as f:
        lines = [line.split() for line in f.readlines()]

    knots = [Knot(0, 0) for _ in range(knot_amount)]

    for line in lines:
        direction = line[0]
        val = int(line[1])

        for idx, knot in enumerate(knots):
            if idx == 0:
                knots[idx].move(direction, val)
                continue
            if not knot.touches(knots[idx-1]):
                knot.follow(knots[idx-1])
        x = []
        y = []
        x += [k.x for k in knots]
        y += [k.y for k in knots]
        plt.plot(x, y, 'bo')
        plt.grid()
        plt.axis([knot_amount*-5, knot_amount*5, knot_amount*-5, knot_amount*5])
        plt.show()

    return len(knots[-1].history)


# print("p1 (Example):", main("input_example_p1.txt", 2))
# print("p2 (Example):", main("input_example_p2.txt", 10))
# print("p1:", main("input.txt", 2))
print("p2:", main("input.txt", 10))

