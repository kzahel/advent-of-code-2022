lines = [l for l in open("2.input").readlines() if l.strip()]

input = [l.strip().split(" ") for l in lines]

# print(lines)

movealias = {
    "A": "R",
    "B": "P",
    "C": "S",
}

shapescore = {
    "R": 1,
    "P": 2,
    "S": 3,
}

outcomescore = {
    "W": 6,
    "D": 3,
    "L": 0,
}

guessmapping = {
    "Y": "P",
    "X": "R",
    "Z": "S",
}

realmapping = {
    "Y": "D",
    "X": "L",
    "Z": "W",
}

winmap = {
    "R": "P",
    "P": "S",
    "S": "R",
}

losemap = {
    "P": "R",
    "S": "P",
    "R": "S",
}


def getoutcome(p1, p2):
    if p1 == p2:
        return "D"
    if p1 == "R":
        if p2 == "S":
            return "L"
        if p2 == "P":
            return "W"
    if p1 == "S":
        if p2 == "R":
            return "W"
        if p2 == "P":
            return "L"
    if p1 == "P":
        if p2 == "R":
            return "L"
        if p2 == "S":
            return "W"


def getoutcomescore(p1, p2):
    # reversed oops
    wlscore = outcomescore[getoutcome(p1, p2)]

    movescore = shapescore[p2]

    return wlscore + movescore


def processmove(arr):
    p1 = movealias[arr[0]]
    p2 = guessmapping[arr[1]]

    score = getoutcomescore(p1, p2)

    print("for", p1, p2, "score was", score)
    return score


def processmoves(arrs):
    total = 0
    for arr in arrs:
        total += processmove(arr)
    print("total score", total)
    return total


# print(processmoves([["A", "Y"], ["B", "X"], ["C", "Z"]]))
# print(processmoves(input))
# print("END P1")


def processmove2(arr):
    p1 = movealias[arr[0]]
    choice = realmapping[arr[1]]

    if choice == "D":
        p2 = p1
    elif choice == "W":
        p2 = winmap[p1]
    elif choice == "L":
        p2 = losemap[p1]

    score = getoutcomescore(p1, p2)

    print("for", p1, p2, "with", choice, "score was", score)
    return score


def processmoves2(arrs):
    total = 0
    for arr in arrs:
        total += processmove2(arr)
    print("total score", total)
    return total


# print(processmoves2([["A", "Y"], ["B", "X"], ["C", "Z"]]))
print(processmoves2(input))
