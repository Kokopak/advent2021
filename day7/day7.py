import sys

with open("input.txt") as f:
    crabs_pos = list(map(int, f.readline().split(",")))

# part 1
minim_fuel = sum(crabs_pos)

for i in range(max(crabs_pos)):
    s = sum(map(lambda x: abs(x - i), crabs_pos))

    if s < minim_fuel:
        minim_fuel = s

print(minim_fuel)

# part 2
minim_fuel = sys.maxsize

for i in range(max(crabs_pos)):
    s = int(sum([((abs(x - i)) * (2 + (abs(x - i) - 1))) / 2 for x in crabs_pos]))

    if s < minim_fuel:
        minim_fuel = s

print(minim_fuel)
