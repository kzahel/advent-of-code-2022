rawexample = """
30373
25512
65332
33549
35390
"""

raw = open("8.input").read()

# raw = rawexample

lines = [l for l in raw.split("\n") if l.strip()]

print(lines)

rows = [list(map(int, l)) for l in lines]
print(rows)
board = rows

numrows = len(rows)
numcols = len(rows[0])


def inbounds(row, col):
    return row >= 0 and col >= 0 and row < numrows and col < numcols


def visible(row, col):
    print("check visible", row, col)
    if row == 0 or col == 0 or row == numrows - 1 or col == numcols - 1:
        return True
    else:
        # need to check
        # look left
        curh = board[row][col]
        print("treehouse h=", curh)

        haspath = False

        for vec in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            i = 1
            while True:
                v = (vec[0] * i, vec[1] * i)
                newpos = (row + v[0], col + v[1])
                print("check", newpos)

                if inbounds(newpos[0], newpos[1]):
                    if board[newpos[0]][newpos[1]] >= curh:
                        haspath = False
                        break
                else:
                    haspath = True
                    break
                i += 1
            if haspath:
                break

        return haspath


if False:
    assert visible(1, 1) == True
    assert visible(1, 2) == True
    assert visible(1, 3) == False
    assert visible(2, 2) == False
    assert visible(3, 2) == True

import time


def computevisibleset():
    visibles = []
    for row in range(numrows):
        for col in range(numcols):
            # time.sleep(0.1)
            if visible(row, col):
                visibles.append((row, col))
    return visibles


import json


def getviewdist(row, col):
    print("check visible", row, col)
    # need to check
    # look left
    curh = board[row][col]
    print("treehouse h=", curh)

    viewdists = [0, 0, 0, 0]

    for j, vec in enumerate(((-1, 0), (1, 0), (0, -1), (0, 1))):
        i = 1
        while True:
            v = (vec[0] * i, vec[1] * i)
            newpos = (row + v[0], col + v[1])
            print("check", newpos)

            if inbounds(newpos[0], newpos[1]):
                viewdists[j] += 1

                if board[newpos[0]][newpos[1]] >= curh:
                    break
            else:
                break
            i += 1

    return viewdists


def part1():
    print(len(computevisibleset()))


import math


def part2():
    mval = 0
    for r in range(numrows):
        for c in range(numcols):
            dists = getviewdist(r, c)
            val = math.prod(dists)

            if val > mval:
                mval = val
    return mval


print(part2())
