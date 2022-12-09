rawexample = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""
rawexample2 = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""

raw = open("9.input").read()

# raw = rawexample2

lines = [l for l in raw.split("\n") if l.strip()]

print(lines)


def parse():
    moves = []
    for line in lines:
        move, count = line.split(" ")
        vec = vecmap[move]
        count = int(count)

        moves.append({"move": move, "vec": vec, "count": count})
    return moves


vecmap = {
    "R": (0, 1),
    "U": (-1, 0),
    "L": (0, -1),
    "D": (1, 0),
}
import itertools


class Map:
    def __init__(self):
        self.head = [0, 0]
        self.tail = [0, 0]

        self.seen = {0: {0: True}}

    def addseen(self, row, col):
        if row not in self.seen:
            self.seen[row] = {}
        if col not in self.seen[row]:
            self.seen[row][col] = True

    def movehead(self, vec):
        self.head[0] += vec[0]
        self.head[1] += vec[1]

        if abs(self.head[0] - self.tail[0]) > 1 or abs(self.head[1] - self.tail[1]) > 1:
            # need to move!

            best = None
            bestvec = None
            for vec in itertools.product([0, 1, -1], [0, 1, -1]):
                newtail = [self.tail[0] + vec[0], self.tail[1] + vec[1]]
                dist = abs(self.head[0] - newtail[0]) + abs(self.head[1] - newtail[1])
                if best is None:
                    best = dist
                    bestvec = vec
                elif dist < best:
                    best = dist
                    bestvec = vec

            self.tail[0] += bestvec[0]
            self.tail[1] += bestvec[1]

            self.addseen(self.tail[0], self.tail[1])

    def getcount(self):
        total = 0
        for row in self.seen:
            total += len(self.seen[row].keys())
        return total


class MultiMap:
    def __init__(self):
        self.knots = [[0, 0] for _ in range(10)]

        self.seen = {0: {0: True}}

    def addseen(self, row, col):
        if row not in self.seen:
            self.seen[row] = {}
        if col not in self.seen[row]:
            self.seen[row][col] = True

    def movehead(self, vec):
        head = self.knots[0]

        head[0] += vec[0]
        head[1] += vec[1]

        for i in range(9):
            prevknot = self.knots[i]
            curknot = self.knots[i + 1]

            if abs(prevknot[0] - curknot[0]) > 1 or abs(prevknot[1] - curknot[1]) > 1:
                # need to move!

                best = None
                bestvec = None
                for vec in itertools.product([0, 1, -1], [0, 1, -1]):
                    newtail = [curknot[0] + vec[0], curknot[1] + vec[1]]
                    dist = abs(prevknot[0] - newtail[0]) + abs(prevknot[1] - newtail[1])
                    if best is None:
                        best = dist
                        bestvec = vec
                    elif dist < best:
                        best = dist
                        bestvec = vec

                curknot[0] += bestvec[0]
                curknot[1] += bestvec[1]

                # self.addseen(self.tail[0], self.tail[1])

        self.addseen(self.knots[-1][0], self.knots[-1][1])

    def getcount(self):
        total = 0
        for row in self.seen:
            total += len(self.seen[row].keys())
        return total


def part1():
    import json

    m = Map()
    moves = parse()
    for move in moves:
        for i in range(move["count"]):
            m.movehead(move["vec"])

    print(m.getcount())
    # print(json.dumps(parse(), indent=2))


# part1()


def part2():

    m = MultiMap()
    moves = parse()
    for move in moves:
        for i in range(move["count"]):
            m.movehead(move["vec"])

    print(m.getcount())
    # print(json.dumps(parse(), indent=2))


print(part2())
