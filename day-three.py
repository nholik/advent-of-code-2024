def check_status(line, idx, curr_status):
    # print(f"Checking status at {idx}")
    if idx < 4:
        return curr_status

    if line[idx - 4 : idx] == "do()":
        return True

    if idx < 7:
        return curr_status

    # print(line[idx - 7 : idx])

    if line[idx - 7 : idx] == "don't()":
        return False

    return curr_status


def process_line(line, enabled, allow_toggle=False):
    result = 0
    i = 4
    status = enabled
    # print(f"Starting line with status: {enabled} - len = {len(line)}")
    if allow_toggle:
        status = check_status(line, i, status)

    while i < len(line):
        if (
            line[i - 4] == "m"
            and line[i - 3] == "u"
            and line[i - 2] == "l"
            and line[i - 1] == "("
        ):
            lhs = 0
            rhs = 0
            while i < len(line) and line[i].isdigit():
                lhs *= 10
                lhs += int(line[i])
                i += 1
                if allow_toggle:
                    status = check_status(line, i, status)
            if i < len(line) and line[i] == ",":
                i += 1
                if allow_toggle:
                    status = check_status(line, i, status)
                while i < len(line) and line[i].isdigit():
                    rhs *= 10
                    rhs += int(line[i])
                    i += 1
                    if allow_toggle:
                        status = check_status(line, i, status)

                if line[i] == ")":
                    if status:
                        result += lhs * rhs
                    i += 1
                    if allow_toggle:
                        status = check_status(line, i, status)
            else:
                i += 1
                if allow_toggle:
                    status = check_status(line, i, status)
        else:
            i += 1
            if allow_toggle:
                status = check_status(line, i, status)

    return result, status


result_part_one = 0

with open("./data/3/input.txt", "r", encoding="utf-8") as f:
    for line in f:
        line_result, _ = process_line(line, True)
        result_part_one += line_result

print(f"Day three part one: {result_part_one}")

result_part_two = 0

with open("./data/3/input.txt", "r", encoding="utf-8") as f:
    enabled = True
    for line in f:
        line_result, curr_status = process_line(line, enabled, True)
        enabled = curr_status
        result_part_two += line_result

print(f"Day three part two: {result_part_two}")
