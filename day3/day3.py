with open("input.txt") as f:
    bits = [l.strip() for l in f.readlines()]

gamma_rate = ""
epsilon_rate = ""

column_bits = list(zip(*bits))

for column in column_bits:
    if column.count("1") > column.count("0"):
        gamma_rate += "1"
        epsilon_rate += "0"
    elif column.count("1") < column.count("0"):
        gamma_rate += "0"
        epsilon_rate += "1"

print(int(gamma_rate, 2) * int(epsilon_rate, 2))


def get_rating(char_1, char_2):
    final_bits = ""

    for i in range(len(bits[0])):
        match_bits = [b for b in bits if b.startswith(final_bits)]
        
        if len(match_bits) == 1:
            return match_bits[0]
        
        column_bits = list(zip(*match_bits))
        column = column_bits[i]

        if column.count("1") > column.count("0"):
            final_bits += char_1
        elif column.count("1") < column.count("0"):
            final_bits += char_2
        else:
            final_bits += char_1
    
    return final_bits

oxygen = int(get_rating("1", "0"), 2)
co2 = int(get_rating("0", "1"), 2)

print(oxygen*co2)

