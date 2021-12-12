cavern = {}

with open("input.txt") as f:
    for r, l in enumerate(f.readlines()):
        for c, n in enumerate(list(l.strip())):
            cavern[(r, c)] = int(n)

POS = [(i, j) for i in range(-1, 2) for j in range(-1, 2)]


step_cavern_memo = {}
step_count = 0


def flash(octo, flashed, cavern):
    global step_count

    step_count += 1
    r_octo, c_octo = octo

    flashed.append(octo)

    for pos in POS:
        r_pos, c_pos = pos
        new_octo = (r_octo + r_pos, c_octo + c_pos)

        if new_octo in cavern:
            cavern[new_octo] += 1

    for octo in cavern:
        if cavern[octo] > 9 and octo not in flashed:
            flash(octo, flashed, cavern)

            cavern[octo] = 0


def step(n, cavern):
    global step_count
    step_count = 0

    for i in range(n):
        step_cavern_memo[i] = cavern

        if i + 1 not in step_cavern_memo:
            cavern = {k: v + 1 for k, v in cavern.items()}

            for octo in cavern:
                if cavern[octo] > 9:
                    flash(octo, [], cavern)
                    cavern[octo] = 0
        else:
            cavern = step_cavern_memo[i + 1]

    return cavern


new_cavern = cavern
n = 0
step(100, cavern)
print(step_count)

while not all(v == 0 for v in new_cavern.values()):
    new_cavern = step(n, cavern)
    n += 1

print(n - 1)
