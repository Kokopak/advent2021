with open("input.txt") as f:
    depths = [int(l.strip()) for l in f.readlines()]

inc = 0
for i in range(len(depths)):
    if i > 0 :
        if depths[i] > depths[i-1]:
            inc += 1
print(inc)

depths_pack = [depths[i:i+3] for i in range(0, len(depths))]

inc = 0
for i in range(len(depths_pack)):
    if i > 0:
        if sum(depths_pack[i]) > sum(depths_pack[i-1]):
            inc += 1
print(inc)    