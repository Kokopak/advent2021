
pos = {}

with open("input.txt") as f:
    positions = [l.split(" ") for l in f.readlines()]

for p in positions:
    cmd, unit = p[0], int(p[1])

    if cmd in pos:
        pos[cmd] += unit
    else:
        pos[cmd] = unit

print((pos["down"] - pos["up"])*pos["forward"])

aim = 0
pos = {"depth": 0, "hpos": 0}

for p in positions:
    cmd, unit = p[0], int(p[1])

    if cmd == "forward":
        pos["hpos"] += unit
        pos["depth"] += unit * aim
    
    if cmd == "down":
        aim += unit
    
    if cmd == "up":
        aim -= unit
    
print(pos["depth"] * pos["hpos"])


