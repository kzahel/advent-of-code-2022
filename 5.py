rawexample = """
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

raw = open("5.input").read()
# raw = rawexample


def parseboard(board):
    arr = board.split("\n")[:-1]

    width = len(arr[-1])
    import math

    w = math.ceil(width / 4)

    cols = [[] for _ in range(w)]

    for line in reversed(arr):

        for i in range(w):
            idx = 1 + (i * 4)
            if idx < len(line):
                char = line[idx]
                if char != " ":
                    cols[i].append(char)

    return cols


def parsemoves(moves):
    outmoves = []
    for move in moves:
        print("move", move)
        parts = move.split(" ")
        print("parts", parts)
        count = int(parts[1])
        fromloc = int(parts[3]) - 1
        toloc = int(parts[5]) - 1
        outmoves.append(dict(count=count, fromloc=fromloc, toloc=toloc))

    return outmoves


def parse(raw):
    board, moves = raw.split("\n\n")

    board = parseboard(board)
    moves = parsemoves([l for l in moves.split("\n") if l.strip()])

    print("parsed", board, moves)

    print(board, moves)
    return board, moves


def gettops(board):
    arr = []
    for col in board:
        if len(col):
            arr.append(col[-1])
    return "".join(arr)


def part1():
    board, moves = parse(raw)
    for move in moves:
        print("doing", move)
        for i in range(move["count"]):
            domove(board, move["fromloc"], move["toloc"])
    print(gettops(board))


def domove(board, fromloc, toloc):
    topitem = board[fromloc][-1]
    board[fromloc] = board[fromloc][:-1]
    board[toloc].append(topitem)
    print("board now", board)


def domove2(board, fromloc, toloc, count):
    topitems = board[fromloc][len(board[fromloc]) - count :]
    board[fromloc] = board[fromloc][:-count]
    for item in topitems:
        board[toloc].append(item)
    print("board now", board)


def part2():
    board, moves = parse(raw)
    for move in moves:
        print("doing", move)
        domove2(board, move["fromloc"], move["toloc"], move["count"])
    print(gettops(board))


# part1()

part2()
