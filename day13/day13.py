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

sheet = np.zeros((height, width))

for coord in coords:
    x, y = coord
    sheet[y, x] = 1

for i, instruction in enumerate(instructions):
    axis, coord = instruction
    if axis == "y":
        cropped = sheet[:coord, :]
        flipped = np.flipud(sheet[coord + 1 :, :])
    else:
        cropped = sheet[:, :coord]
        flipped = np.fliplr(sheet[:, coord + 1 :])

    sheet = np.logical_or(cropped, flipped).astype(int)

    # p1
    if i == 0:
        print(np.sum(sheet))

for y in range(len(sheet)):
    for x in range(len(sheet[0, :])):
        print(sheet[y, x] if sheet[y, x] else " ", end="")
    print()
