patterns_outputs = []
with open("input.txt") as f:
    for l in f.readlines():
        pattern_string, output_string = l.split(" | ")

        patterns_outputs.append(
            (pattern_string.strip().split(" "), output_string.strip().split(" "))
        )


NB_SEGMENTS = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
CONTAINS = {
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

# part 1

s = []
for po in patterns_outputs:
    s.extend(
        [
            output
            for output in po[1]
            if len(output)
            in [NB_SEGMENTS[1], NB_SEGMENTS[4], NB_SEGMENTS[7], NB_SEGMENTS[8]]
        ]
    )

print(len(s))

# part 2


def get_decode(dcd, patterns):
    to_try = set()

    for pattern in patterns:
        set_pattern = set(pattern)

        for p_decode, decode in dcd.items():
            set_decode = set(p_decode)

            if not set_decode.issubset(set_pattern) and not set_pattern.issubset(
                set_decode
            ):
                if pattern in dcd:
                    for cont in CONTAINS[dcd[pattern]]:
                        if decode == cont:

                            return False
            else:
                if not pattern in dcd:
                    for cont in CONTAINS[dcd[p_decode]]:
                        if (
                            cont not in dcd.values()
                            and len(pattern) == NB_SEGMENTS[cont]
                        ):
                            to_try.add((pattern, cont))

    if not len(to_try):
        for pattern in patterns:
            if pattern not in dcd:
                for nb, nb_seg in enumerate(NB_SEGMENTS):
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
            NB_SEGMENTS[1],
            NB_SEGMENTS[4],
            NB_SEGMENTS[7],
            NB_SEGMENTS[8],
        ]:
            decoded_dict[pattern] = NB_SEGMENTS.index(len(pattern))

    decoded = get_decode(decoded_dict, patterns)
    decoded_sorted = {"".join(sorted(k)): v for k, v in decoded.items()}
    decoded_output = int(
        "".join(
            map(str, [decoded_sorted["".join(sorted(output))] for output in outputs])
        )
    )

    s += decoded_output

print(s)
