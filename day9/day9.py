heightmap = {}
height = 0
width = 0

with open("input.txt") as f:
    for r, l in enumerate(f.readlines()):
        height += 1
        width = 0

        for c, n in enumerate(list(l.strip())):
            heightmap[(r, c)] = int(n)
            width += 1


POS = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if abs(i) != abs(j)]

# part 1

lower_points = set()
low_points = 0

for point in heightmap:
    lower = 0
    r_point, c_point = point

    for pos in POS:
        r_pos, c_pos = pos

        new_r_point, new_c_point = (r_point + r_pos, c_point + c_pos)

        if (new_r_point, new_c_point) in heightmap:
            if heightmap[(new_r_point, new_c_point)] > heightmap[point]:
                lower += 1

    if point in [(0, 0), (0, width - 1), (height - 1, 0), (height - 1, width - 1)]:
        if lower == 2:
            low_points += 1 + heightmap[point]
            lower_points.add(point)
    elif r_point == 0 or r_point == height - 1 or c_point == 0 or c_point == width - 1:
        if lower == 3:
            low_points += 1 + heightmap[point]
            lower_points.add(point)
    else:
        if lower == 4:
            low_points += 1 + heightmap[point]
            lower_points.add(point)

print(low_points)

# part 2

POS = [(i, j) for i in range(-1, 2) for j in range(-1, 2)]


def find_basin(point, basins=set()):
    basins.add(point)

    r_point, c_point = point

    new_points = False

    for pos in POS:
        r_pos, c_pos = pos
        new_r_point, new_c_point = (r_point + r_pos, c_point + c_pos)

        print(point, "-", (new_r_point, new_c_point))

        if (new_r_point, new_c_point) in heightmap and (
            new_r_point,
            new_c_point,
        ) not in basins:
            if heightmap[(new_r_point, new_c_point)] != 9:
                basins.add((new_r_point, new_c_point))
                new_points = True

    if new_points:
        for basin in basins:
            fb = find_basin(basin, basins)

            if fb:
                basins.update(fb)
                return basins
    else:

        return basins


print(find_basin((0, 1)))
