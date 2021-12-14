from collections import defaultdict

with open("input.txt") as f:
    polymer, rules = f.read().strip().split("\n\n")

polymer = polymer.strip()
rules = {r.split(" -> ")[0]: r.split(" -> ")[1] for r in rules.split("\n")}

pair_counter = defaultdict(int)
letter_counter = defaultdict(int)

for i in range(len(polymer) - 1):
    pair_counter[polymer[i : i + 2]] += 1

for m in polymer:
    letter_counter[m] += 1

for i in range(40):
    old_pair_counter = pair_counter.copy()
    for pair in old_pair_counter:

        if old_pair_counter[pair] > 0:
            mol, next_mol = list(pair)

            pair_counter[f"{mol}{rules[pair]}"] += old_pair_counter[pair]
            pair_counter[f"{rules[pair]}{next_mol}"] += old_pair_counter[pair]

            letter_counter[rules[pair]] += old_pair_counter[pair]

        pair_counter[pair] -= old_pair_counter[pair]

    # p1
    if i == 9:
        print(max(letter_counter.values()) - min(letter_counter.values()))

# p2
print(max(letter_counter.values()) - min(letter_counter.values()))
