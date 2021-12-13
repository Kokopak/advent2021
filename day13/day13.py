import numpy as np

instructions = []
with open("input.txt") as f:
    coords = []
    is_instruction = False
    for l in f.readlines():
        l = l.strip()

        if l != "" and not is_instruction:
            x, y = map(int, l.split(","))
            coords.append((x, y))
        else:
            is_instruction = True

        if is_instruction:
            if l:
                axis, coord = l.split(" ")[-1].split("=")
                instructions.append((axis, int(coord)))

height = max(coords, key=lambda x: x[1])[1] + 1
width = max(coords, key=lambda x: x[0])[0] + 1

sheet = [[0 for x in range(width)] for y in range(height)]

for coord in coords:
    x, y = coord
    sheet[y][x] = 1

sheet = np.array(sheet)
new_sheet = np.copy(sheet)

for i, instruction in enumerate(instructions):
    axis, coord = instruction
    if axis == "y":
        cropped = new_sheet[:coord, :]
        flipped = np.flipud(new_sheet[coord + 1 :, :])
    else:
        cropped = new_sheet[:, :coord]
        flipped = np.fliplr(new_sheet[:, coord + 1 :])

    width_cropped = len(cropped[0, :])
    height_cropped = len(cropped)

    new_sheet = np.array(
        [
            [1 if cropped[y, x] or flipped[y, x] else 0 for x in range(width_cropped)]
            for y in range(height_cropped)
        ]
    )

    # p1
    if i == 0:
        print(np.sum(new_sheet))

for y in range(len(new_sheet)):
    for x in range(len(new_sheet[0, :])):
        print(new_sheet[y, x] if new_sheet[y, x] else " ", end="")
    print()
