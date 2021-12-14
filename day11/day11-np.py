import numpy as np


cavern = np.genfromtxt("./input.txt", delimiter=10 * (1,)).astype(int)


def check_flash(flashed):
    total = 0
    for i, j in np.argwhere(cavern > 9):
        if (i, j) not in flashed:
            left = j - 1 if j - 1 >= 0 else 0
            right = j + 1 if j + 1 <= 9 else 9
            up = i - 1 if i - 1 >= 0 else 0
            down = i + 1 if i + 1 <= 9 else 9

            cavern[up : down + 1, left : right + 1] += 1
            flashed.add((i, j))
            total += 1
            total += check_flash(flashed)

    return total


s = 0
step = 0

while not np.all(cavern == 0):
    cavern += 1

    flashed = set([])
    s += check_flash(flashed)

    cavern[cavern > 9] = 0

    # p1
    if step == 99:
        print(s)

    step += 1

# p2
print(step)
