from collections import Counter

patterns_outputs = []
with open("input2.txt") as f:
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

inv_contains = {
    0: [1, 7],
    1: [],
    2: [],
    3: [1, 7],
    4: [1],
    5: [],
    6: [5],
    7: [1],
    8: [0, 1, 2, 3, 4, 5, 6, 7, 9],
    9: [1, 3, 4, 5, 7],
}


def get_decode(dcd, patterns):
    # print(dcd)
    nb_segments = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

    for k, v in dcd.items():
        if v == 4:
            FOUR = k

    if list(sorted(dcd.values())) == list(range(10)):
        return dcd

    to_try = set()
    for pattern in patterns:
        if pattern not in dcd:
            set_pattern = set(pattern)
            find = []

            for decode in dcd:
                set_decode = set(decode)

                if set_decode.issubset(set_pattern) or set_pattern.issubset(set_decode):
                    for cont in contains[dcd[decode]]:
                        if (
                            cont not in dcd.values()
                            and len(pattern) == nb_segments[cont]
                        ):
                            if cont == 0 or cont == 9:
                                if set(FOUR).issubset(set_pattern):
                                    to_try.add((pattern, 9))
                                else:
                                    to_try.add((pattern, 0))
                            else:
                                to_try.add((pattern, cont))

    if not len(to_try):
        for pattern in patterns:
            if pattern not in dcd:
                for nb, nb_seg in enumerate(nb_segments):
                    if nb_seg == len(pattern) and nb not in dcd.values():
                        to_try.add((pattern, nb))
    for tt in to_try:
        p, nb = tt
        dcd_tmp = dcd.copy()
        dcd_tmp[p] = nb
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

    decoded_sorted = {"".join(sorted(k)): v for k, v in decoded.items()}
    decoded_output = []
    for output in outputs:
        output_sorted = "".join(sorted(output))
        decoded_output.append(decoded_sorted[output_sorted])

    print(decoded_output)
