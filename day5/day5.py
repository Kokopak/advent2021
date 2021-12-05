vents = []
max_coord = [0, 0]
with open("input.txt") as f:
    for l in f.readlines():
        l = l.strip().split(" -> ")
        coord1 = tuple(map(int, l[0].split(",")))
        coord2 = tuple(map(int, l[1].split(",")))
        vents.append((coord1, coord2))

        max_coord[0] = (
            coord1[0]
            if coord1[0] > max_coord[0]
            else coord2[0]
            if coord2[0] > max_coord[0]
            else max_coord[0]
        )

        max_coord[1] = (
            coord1[1]
            if coord1[1] > max_coord[1]
            else coord2[1]
            if coord2[1] > max_coord[1]
            else max_coord[1]
        )


def count_covered(moves):
    cover = {}

    for vent in vents:
        (x1, y1), (x2, y2) = vent

        for move in moves:
            mx, my = x1, y1
            move_coord = (mx, my)
            covered_coords = [move_coord]

            while (
                move_coord != (x2, y2)
                and move_coord[0] >= 0
                and move_coord[0] <= max_coord[0]
                and move_coord[1] >= 0
                and move_coord[1] <= max_coord[1]
            ):
                mx += move[0]
                my += move[1]
                move_coord = (mx, my)

                covered_coords.append(move_coord)

            if (mx, my) == (x2, y2):
                for c in covered_coords:
                    if c in cover:
                        cover[c] += 1
                    else:
                        cover[c] = 1

    count_covered = 0
    for cov in cover:
        if cover[cov] >= 2:
            count_covered += 1

    return count_covered


print(
    count_covered(moves=[(-1, 0), (1, 0), (0, 1), (0, -1)]),
    count_covered(
        moves=[(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    ),
)
