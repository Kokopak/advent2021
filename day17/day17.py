import re

with open("input.txt") as f:
    l = f.read()

    r = re.search(r"target area: x=(-?[0-9]+)..(-?[0-9]+), y=(-?[0-9]+)..(-?[0-9]+)", l)

    range_x = range(int(r.group(1)), int(r.group(2)) + 1)
    range_y = range(int(r.group(3)), int(r.group(4)) + 1)

probe_pos = [0, 0]


def step(probe_pos, vel_x, vel_y, range_x, range_y, seen, max_y):
    copy = probe_pos[:]

    if copy not in seen:
        seen.append(copy)

    if copy[0] in range_x and copy[1] in range_y:
        return True, max_y

    if copy[0] > list(range_x)[-1] or copy[1] < list(range_y)[1]:
        return False, 0

    copy[0] += vel_x if vel_x > 0 else 0
    copy[1] += vel_y

    if copy[1] > max_y:
        max_y = copy[1]

    if copy[0] > 0:
        vel_x -= 1
    elif copy[0] < 0:
        vel_x += 1
    else:
        vel_x = 0

    vel_y -= 1

    return step(copy, vel_x, vel_y, range_x, range_y, seen, max_y)


max_y = 0
sum_sh = 0
for x in range(list(range_x)[-1] + 1):
    for y in range(list(range_y)[0], abs(list(range_y)[0])):
        s = step([0, 0], x, y, range_x, range_y, [], 0)

        if s[0]:
            sum_sh += 1

            if s[1] > max_y:
                max_y = s[1]


print(max_y)
print(sum_sh)
