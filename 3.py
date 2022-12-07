data = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

# lines = data.split("\n")
lines = open("3.input").readlines()

lines = [l.strip() for l in lines if l.strip()]

input = [(l[: int(len(l) / 2)], l[int(len(l) / 2) :]) for l in lines]

print(lines)
print(input)


def getgroups(lines):
    all = []
    for i in range(int(len(lines) / 3)):
        slice = lines[i * 3 : 3 * (i + 1)]
        all.append(slice)
    return all


# print(getgroups(lines))


def getshared(packs):
    for char in packs[0]:
        if char in packs[1] and char in packs[2]:
            return char


def getscore(letter):
    if letter.lower() == letter:
        p = ord(letter) - ord("a") + 1
    else:
        p = ord(letter) - ord("A") + 27
    return p


def finddupe(a, b):
    for char in a:
        if char in b:
            return char


def getanswer():
    total = 0
    for (a, b) in input:
        char = finddupe(a, b)
        score = getscore(char)
        total += score
        print("char score", char, score)
    return total


# print("getanswer", getanswer())


def part2():
    total = 0
    for group in getgroups(lines):
        char = getshared(group)
        score = getscore(char)
        total += score
    print("total", total)


part2()
