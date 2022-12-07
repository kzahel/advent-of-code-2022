rawexample = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""
raw = open("7.input").read()

# raw = rawexample

lines = [l for l in raw.split("\n") if l.strip()]

print(lines)


class FS:
    def __init__(self):
        self.data = {"files": [], "dirs": {}}

    def add(self, cwd, name, size, node=None):
        if node is None:
            node = self.data

        if len(cwd) == 0:
            node["files"].append({"name": name, "size": size})
        else:
            self.add(cwd[1:], name, size, node["dirs"][cwd[0]])

    def adddir(self, cwd, name, node=None):
        if node is None:
            node = self.data

        if len(cwd) == 0:
            node["dirs"][name] = {"files": [], "dirs": {}}
        else:
            self.adddir(cwd[1:], name, node["dirs"][cwd[0]])

    def debug(self):
        import json

        print(json.dumps(self.data, indent=2))

    def walk(self, path=None, node=None):
        if node is None:
            node = self.data
            path = []

        for dirname in node["dirs"]:
            yield path + [dirname]
            subiter = self.walk(path + [dirname], node["dirs"][dirname])
            yield from subiter

    def getdir(self, path, node=None):
        if node is None:
            node = self.data
        if len(path) == 0:
            return node
        else:
            return self.getdir(path[1:], node["dirs"][path[0]])


def getsize(data):
    total = 0
    herecount = sum([f["size"] for f in data["files"]])
    total += herecount
    for dirname, subdata in data["dirs"].items():
        total += getsize(subdata)
    return total


def parse(lines):
    cwd = []

    fs = FS()

    for line in lines:
        print(line)
        if line.startswith("$ "):
            parts = line.split(" ")
            command = parts[1]
            if command == "cd":
                path = parts[2]
                if path == "/":
                    cwd = []
                elif path == "..":
                    cwd = cwd[:-1]
                else:
                    cwd.append(path)
        elif line.startswith("dir "):
            name = line.split(" ")[1]
            fs.adddir(cwd, name)
            print("add dir", cwd, name)
            fs.debug()
        else:
            parts = line.split(" ")
            size = int(parts[0])
            name = parts[1]
            fs.add(cwd, name, size)
            print("add file", cwd, name, size)
            fs.debug()
    return fs


fs = parse(lines)
# print(fs.data)


def part1():
    fs = parse(lines)
    final = 0
    for dirname in fs.walk():
        dir = fs.getdir(dirname)
        sz = getsize(dir)
        print("dir with sz", dirname, sz)
        if sz < 100_000:
            final += sz
    print("final answer", final)


# part1()


def part2():
    total = 70_000_000
    req = 30_000_000

    candidates = []

    total_used = getsize(fs.getdir([]))

    available = total - total_used

    for dirname in fs.walk():
        dir = fs.getdir(dirname)
        sz = getsize(dir)
        print("dir with sz", dirname, sz)
        if available + sz >= req:
            print("found candidate", dir)
            candidates.append(dirname)

    candidates.reverse()

    summary = [(c, getsize(fs.getdir(c))) for c in candidates]
    summary.sort(key=lambda x: x[1])
    import json

    print("summary", json.dumps(summary, indent=2))
    print("final answer", summary[0])


part2()
