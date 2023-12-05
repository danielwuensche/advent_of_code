class Knot:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.history = {(self.x, self.y)}

    def __str__(self):
        return f"Knot({self.x}, {self.y})"

    __repr__ = __str__

    def move(self, direction: str, val: int) -> None:
        match direction:
            case "R":
                self.x += val
            case "L":
                self.x -= val
            case "U":
                self.y += val
            case "D":
                self.y -= val

    def touches(self, other):
        return True if (self.x in [other.x-1, other.x, other.x+1] and
                        self.y in [other.y-1, other.y, other.y+1]) else False

    def follow(self, other):
        while not self.touches(other):
            if self.x < other.x:
                self.x += 1
            elif self.x > other.x:
                self.x -= 1

            if self.y < other.y:
                self.y += 1
            elif self.y > other.y:
                self.y -= 1

            self.history.add((self.x, self.y))
