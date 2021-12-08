patterns_outputs = []
with open("input.txt") as f:
    for l in f.readlines():
        pattern_string, output_string = l.split(" | ")

        patterns_outputs.append(
            (pattern_string.strip().split(" "), output_string.strip().split(" "))
        )


nb_segments = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

# part 1

S_unique_seg = 0
for po in patterns_outputs:
    for output in po[1]:
        if len(output) in [
            nb_segments[1],
            nb_segments[4],
            nb_segments[7],
            nb_segments[8],
        ]:
            S_unique_seg += 1

print(S_unique_seg)

# part 2

contains = {
    0: [8],
    1: [0, 3, 4, 7, 8, 9],
    2: [8],
    3: [8, 9],
    4: [8, 9],
    5: [6, 8, 9],
    6: [8],
    7: [0, 3, 8, 9],
    8: [],
    9: [8],
}


for po in patterns_outputs:
    patterns = po[0]
    decoded = patterns[:]
    decoded_dict = {}

    for i_p, pattern in enumerate(patterns):
        if len(pattern) in [
            nb_segments[1],
            nb_segments[4],
            nb_segments[7],
            nb_segments[8],
        ]:
            decoded[i_p] = nb_segments.index(len(pattern))
            decoded_dict[pattern] = nb_segments.index(len(pattern))
        else:

            print(nb_segments[len(pattern)])

print("\t".join(patterns_outputs[0][0]))
print("\t".join(map(str, decoded)))

print(decoded_dict)
