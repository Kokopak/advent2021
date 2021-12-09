from collections import Counter

patterns_outputs = []
with open("input.txt") as f:
    for l in f.readlines():
        pattern_string, output_string = l.split(" | ")

        patterns_outputs.append(
            (pattern_string.strip().split(" "), output_string.strip().split(" "))
        )


nb_segments = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

# part 1

s = []
for po in patterns_outputs:
    s.extend(
        [
            output
            for output in po[1]
            if len(output)
            in [nb_segments[1], nb_segments[4], nb_segments[7], nb_segments[8]]
        ]
    )

print(len(s))

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


def get_decode(dcd, patterns):
    # print(dcd)
    nb_segments = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

    if list(sorted(dcd.values())) == list(range(10)):
        print("=>", dcd)
        return dcd

    for pattern in patterns:
        if pattern not in dcd:

            set_pattern = set(pattern)
            for decode in dcd:
                set_decode = set(decode)
                if set_decode.issubset(set_pattern):
                    for cont in contains[dcd[decode]]:
                        if (
                            cont not in dcd.values()
                            and len(pattern) == nb_segments[cont]
                        ):
                            dcd_tmp = dcd.copy()
                            dcd_tmp[pattern] = cont
                            gd = get_decode(dcd_tmp, patterns)

                            if gd:
                                return gd

            for nb, nb_segment in enumerate(nb_segments):
                if nb_segment == len(pattern) and nb not in dcd.values():
                    dcd_tmp = dcd.copy()
                    dcd_tmp[pattern] = nb
                    gd = get_decode(dcd_tmp, patterns)
                    if gd:
                        return gd


for po in patterns_outputs:
    decoded_dict = {}
    patterns, outputs = po

    for i_p, pattern in enumerate(patterns):
        if len(pattern) in [
            nb_segments[1],
            nb_segments[4],
            nb_segments[7],
            nb_segments[8],
        ]:
            decoded_dict[pattern] = nb_segments.index(len(pattern))

    decoded = get_decode(
        decoded_dict,
        patterns,
    )
    print(decoded)

    # decoded_sorted = {"".join(sorted(k)): v for k, v in decoded.items()}
    # decoded_output = []
    # for output in outputs:
    #     output_sorted = "".join(sorted(output))
    #     decoded_output.append(decoded_sorted[output_sorted])

    # print(decoded_output)
    # # print([decoded[o] for o in output])
