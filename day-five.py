from collections import defaultdict
from functools import cmp_to_key

l_to_r_map = defaultdict(set)
r_to_l_map = defaultdict(set)

rules = []


def comparator(a, b):
    # print("comparing")
    if b in l_to_r_map[a]:
        # print(f"{a} must come before {b} - {(a,b)}")
        return -1

    if a in r_to_l_map[b]:
        # print(f"{b} must come before {a} - {(a,b)}")
        return 1

    return 0


with open("./data/5/input.txt", "r", encoding="utf-8") as f:
    for line in f:
        stripped = line.strip()
        if len(stripped) > 0:
            if "|" in stripped:
                fst, snd = stripped.split("|")
                l_to_r_map[int(fst)].add(int(snd))
                r_to_l_map[int(snd)].add(int(fst))
            else:
                rules.append([int(num) for num in stripped.split(",")])

key_comp = cmp_to_key(comparator)

result_part_one = 0
result_part_two = 0
for ordering in rules:
    sorted_ording = sorted(ordering, key=key_comp)
    mid = len(ordering) // 2
    if ordering == sorted_ording:
        result_part_one += ordering[mid]
    else:
        result_part_two += sorted_ording[mid]
        # print(f"original: {ordering} - ordered - {sorted_ording}")

print(f"Day five part one: {result_part_one}")
print(f"Day five part two: {result_part_two}")
