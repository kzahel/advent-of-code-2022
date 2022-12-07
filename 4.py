input = open("4.input").read()
inputexample = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

# input = inputexample

lines = [l for l in input.split("\n") if l.strip()]


def parseline(line):
    a1, a2 = line.split(",")

    r1 = list(map(int, a1.split("-")))
    r2 = list(map(int, a2.split("-")))

    return (r1, r2)


def part1():
    total = 0
    for line in lines:
        (r1, r2) = parseline(line)
        if contains(r1, r2):
            print("contained", r1, r2)
            total += 1
    return total


def contains(r1, r2):
    if r1[0] >= r2[0] and r1[1] <= r2[1]:
        return True
    if r2[0] >= r1[0] and r2[1] <= r1[1]:
        return True

    return False


#  aa
#     bb
#
#  bb
#     aa
#
#  aaaa
#    bbbb
#


def overlap(r1, r2):
    if r1[0] < r2[0] and r1[1] < r2[0]:
        return False
    if r2[0] < r1[0] and r2[1] < r1[0]:
        return False
    return True


def part2():
    total = 0
    for line in lines:
        (r1, r2) = parseline(line)
        if overlap(r1, r2):
            print("overlap", r1, r2)
            total += 1
    return total


print(part2())
