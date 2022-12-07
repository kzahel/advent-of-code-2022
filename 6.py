# rawexample = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
# rawexample = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
rawexample = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
raw = open("6.input").read().strip()
# raw = rawexample


def unique(chunk):
    return len(set(chunk)) == len(chunk)


def findstart(raw, chunklen=4):
    i = chunklen
    while True:
        if i >= len(raw):
            break
        if i < len(raw):
            chunk = raw[i - chunklen : i]
            print("inspecting", chunk)
            if unique(chunk):
                print("unique!")
                return i

        i += 1


def part1():
    start = findstart(raw)
    print("found start", start)


def part2():
    start = findstart(raw, chunklen=14)
    print("found start", start)


part2()
