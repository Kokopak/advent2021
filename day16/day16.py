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


def gen_packet_p1(bin_str):
    global S
    if bin_str == [] or len(set(bin_str)) == 1:
        return

    version = int("".join(pop(bin_str, 3)), 2)
    type_id = int("".join(pop(bin_str, 3)), 2)

    S += version

    if type_id == 4:
        print(f"LV {version} +>", "".join(bin_str))
        groups = [
            "".join(pop(bin_str, 5))
            for _ in range(0, len(bin_str), 5)
            if bin_str[0] != "0"
        ]
        groups.append("".join(pop(bin_str, 5)))
        gen_packet_p1(bin_str)
    else:
        print(f"OP {version} {type_id} +>", "".join(bin_str))

        length_type_id = int("".join(pop(bin_str, 1)), 2)

        if length_type_id == 0:
            length_sub_packet = int("".join(pop(bin_str, 15)), 2)
            gen_packet_p1(pop(bin_str, length_sub_packet))
        else:
            number_sub_packets = int("".join(pop(bin_str, 11)), 2)
            for _ in range(number_sub_packets):
                gen_packet_p1(bin_str)

    gen_packet_p1(bin_str)


def gen_packet_p2(bin_str):

    if isinstance(bin_str, int):
        return bin_str

    if bin_str == [] or len(set(bin_str)) == 1:
        return 0

    version = int("".join(pop(bin_str, 3)), 2)
    type_id = int("".join(pop(bin_str, 3)), 2)

    if type_id == 4:
        print(f"LV {version} +>", "".join(bin_str))
        groups = [
            "".join(pop(bin_str, 5))
            for _ in range(0, len(bin_str), 5)
            if bin_str[0] != "0"
        ]
        groups.append("".join(pop(bin_str, 5)))

        return gen_packet_p2(int("".join(groups), 2))
    else:
        print(f"OP {version} {type_id} +>", "".join(bin_str))
        packets = []

        length_type_id = int("".join(pop(bin_str, 1)), 2)

        if length_type_id == 0:
            length_sub_packet = int("".join(pop(bin_str, 15)), 2)
            packet = pop(bin_str, length_sub_packet)
            while packet != "":
                gp2 = gen_packet_p2(packet)
                packets.append(gp2)
        else:
            number_sub_packets = int("".join(pop(bin_str, 11)), 2)
            for _ in range(number_sub_packets):
                gp2 = gen_packet_p2(bin_str)
                packets.append(gp2)

        print(type_id, packets)
        if len(packets):
            # print(type_id, packets, functools.reduce(TYPE_ID_OP[type_id], packets))
            return functools.reduce(TYPE_ID_OP[type_id], packets)

    # return gen_packet_p2(bin_str)


bin_str = list(hex_to_bin("9C0141080250320F1802104A08"))
# gen_packet_p1(bin_str)
# print(S)
gen_packet_p2(bin_str)
