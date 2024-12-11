crossword = []


def in_bounds(x, y):
    result = x >= 0 and x < len(crossword[0]) and y >= 0 and y < len(crossword)
    return result


directions = [(1, 0), (0, 1), (-1, 0), (-1, -1), (0, -1), (1, 1), (1, -1), (-1, 1)]

with open("./data/4/input.txt", "r", encoding="utf-8") as f:
    for line in f:
        crossword.append(list(line.strip()))

trailing_letters = ["M", "A", "S"]

xmas_found = 0

for y in range(len(crossword)):
    for x in range(len(crossword[0])):
        if crossword[y][x] == "X":
            for dx, dy in directions:
                found_letters = 0
                for i, letter in enumerate(trailing_letters):
                    offset_x = x + dx * (i + 1)
                    offset_y = y + dy * (i + 1)
                    if (
                        in_bounds(offset_x, offset_y)
                        and crossword[offset_y][offset_x] == letter
                    ):
                        found_letters += 1
                    else:
                        break

                if found_letters == len(trailing_letters):
                    xmas_found += 1

print(f"Day four part one: {xmas_found}")

cross_a_found = 0
for y in range(len(crossword)):
    for x in range(len(crossword[0])):
        if crossword[y][x] == "A":
            first_slash = (
                in_bounds(x - 1, y - 1)
                and in_bounds(x + 1, y + 1)
                and (
                    (crossword[y - 1][x - 1] == "S" and crossword[y + 1][x + 1] == "M")
                    or (
                        crossword[y - 1][x - 1] == "M"
                        and crossword[y + 1][x + 1] == "S"
                    )
                )
            )
            second_slash = (
                in_bounds(x + 1, y - 1)
                and in_bounds(x - 1, y + 1)
                and (
                    (crossword[y - 1][x + 1] == "S" and crossword[y + 1][x - 1] == "M")
                    or (
                        crossword[y - 1][x + 1] == "M"
                        and crossword[y + 1][x - 1] == "S"
                    )
                )
            )

            if first_slash and second_slash:
                cross_a_found += 1

print(f"Day four part two: {cross_a_found}")
