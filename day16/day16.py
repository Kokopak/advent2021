import functools

HEX_TO_BIN = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

TYPE_ID_OP = {
    0: lambda x, y: x + y,
    1: lambda x, y: x * y,
    2: min,
    3: max,
    5: lambda x, y: 1 if x > y else 0,
    6: lambda x, y: 1 if x < y else 0,
    7: lambda x, y: 1 if x == y else 0,
}


def hex_to_bin(hex_str):
    return "".join([HEX_TO_BIN[s] for s in hex_str])


def pop(bin_str, index):
    ret = bin_str[:index]
    del bin_str[:index]

    return ret


S = 0


def gen_packet(bin_str):
    global S

    if isinstance(bin_str, int):
        return bin_str

    version = int("".join(pop(bin_str, 3)), 2)
    S += version

    type_id = int("".join(pop(bin_str, 3)), 2)

    if type_id == 4:
        groups = [
            "".join(pop(bin_str, 5))[1:5]
            for _ in range(0, len(bin_str), 5)
            if bin_str[0] != "0"
        ]
        groups.append("".join(pop(bin_str, 5))[1:5])

        return int("".join(groups), 2)
    else:
        packets = []

        length_type_id = int("".join(pop(bin_str, 1)), 2)

        if length_type_id == 0:
            length_sub_packet = int("".join(pop(bin_str, 15)), 2)
            packet = pop(bin_str, length_sub_packet)

            while packet != []:
                packets.append(gen_packet(packet))
        else:
            number_sub_packets = int("".join(pop(bin_str, 11)), 2)

            for _ in range(number_sub_packets):
                packets.append(gen_packet(bin_str))

        return functools.reduce(TYPE_ID_OP[type_id], packets)


with open("input.txt") as f:
    bin_str = list(hex_to_bin(f.read()))

print(gen_packet(bin_str))
print(S)
