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
    nb_segments = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

    to_try = set()
    for pattern in patterns:
        set_pattern = set(pattern)

        for p_decode, decode in dcd.items():
            set_decode = set(p_decode)

            if pattern in dcd:
                for cont in contains[dcd[pattern]]:
                    if decode == cont:
                        if not set_decode.issubset(
                            set_pattern
                        ) and not set_pattern.issubset(set_decode):
                            return False
            else:
                if set_decode.issubset(set_pattern) or set_pattern.issubset(set_decode):
                    for cont in contains[dcd[p_decode]]:
                        if (
                            cont not in dcd.values()
                            and len(pattern) == nb_segments[cont]
                        ):
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

    if list(sorted(dcd.values())) == list(range(10)):
        return dcd


s = 0
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

    decoded = get_decode(decoded_dict, patterns)
    decoded_sorted = {"".join(sorted(k)): v for k, v in decoded.items()}
    decoded_output = []

    for output in outputs:
        output_sorted = "".join(sorted(output))
        decoded_output.append(decoded_sorted[output_sorted])

    s += int("".join(map(str, decoded_output)))

print(s)
