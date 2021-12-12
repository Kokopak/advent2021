from collections import defaultdict

chunks = []

with open("input.txt") as f:
    chunks = [l.strip() for l in f.readlines()]

closing_d = {"(": ")", "[": "]", "{": "}", "<": ">"}
errors_p1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
errors_p2 = {")": 1, "]": 2, "}": 3, ">": 4}
scores = []

s = 0

for chunk in chunks:
    level = 0
    levels = defaultdict(str)
    autocomplete_s = ""
    ts = 0

    for c in chunk:
        if c in closing_d:
            level += 1
            levels[level] = c
        else:
            if c == closing_d[levels[level]]:
                del levels[level]
                level -= 1
            else:
                s += errors_p1[c]
                break
    else:
        for i in range(max(levels), 0, -1):
            autocomplete_s += closing_d[levels[i]]

        for ac in autocomplete_s:
            ts = 5 * ts + errors_p2[ac]

        scores.append(ts)

print(s)
print(sorted(scores)[len(scores) // 2])
