from collections import defaultdict


graph = defaultdict(list)
lowercases = set([])

with open("input.txt") as f:
    for l in f.readlines():
        s, e = l.strip().split("-")

        graph[s].append(e)
        graph[e].append(s)

        if s not in ["start", "end"] and not s.isupper():
            lowercases.add(s)
        if e not in ["start", "end"] and not e.isupper():
            lowercases.add(e)

paths = set([])


def find_path_p1(node, path):
    if node == "end":
        paths.add(tuple(path))
        return

    for n in graph[node]:
        tmp_path = path[:]

        if (n.islower() and not n in path) or not n.islower():
            tmp_path.append(n)
            find_path_p1(n, tmp_path)


def can_visit(node, path):
    if node.islower():
        count = 1

        if node not in ["start", "end"]:
            for n in lowercases:
                if path.count(n) > 1:
                    break
            else:
                count = 2

        if path.count(node) < count:
            return True
    else:
        return True

    return False


def find_path_p2(node, path):
    if node == "end":
        paths.add(tuple(path))
        return

    for n in graph[node]:
        tmp_path = path[:]
        if can_visit(n, path):
            tmp_path.append(n)
            find_path_p2(n, tmp_path)


find_path_p1("start", ["start"])
print(len(paths))


paths = set([])
find_path_p2("start", ["start"])
print(len(paths))
