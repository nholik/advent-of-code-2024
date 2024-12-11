def is_safe(items, increasing):
    last_item = items[0]
    for i in range(1, len(items)):
        elt = items[i]
        if increasing and elt <= last_item:
            return 0
        elif not increasing and elt >= last_item:
            return 0

        diff = abs(last_item - elt)

        if diff == 0 or diff > 3:
            return 0

        last_item = elt

    return 1


def find_solution_one():
    safe_count = 0

    with open("./data/2/input.txt", "r", encoding="utf-8") as f:
        for line in f:
            nums = [int(num) for num in line.strip().split(" ")]
            if nums[0] > nums[-1]:
                safe_count += is_safe(nums, False)
            elif nums[0] < nums[-1]:
                safe_count += is_safe(nums, True)
    return safe_count


def create_candidate(items, skip_index):
    output = []
    for i, elt in enumerate(items):
        if i != skip_index:
            output.append(elt)

    return output


def find_solution_two():
    safe_count = 0

    with open("./data/2/input.txt", "r", encoding="utf-8") as f:
        for line in f:
            nums = [int(num) for num in line.strip().split(" ")]
            for i in range(len(nums) + 1):
                items = create_candidate(nums, i - 1)
                if items[0] > items[-1] and (is_safe(items, False) > 0):
                    safe_count += 1
                    break
                elif items[0] < items[-1] and (is_safe(items, True) > 0):
                    safe_count += 1
                    break
    return safe_count


print(f"Day two part one: {find_solution_one()}")
print(f"Day two part two: {find_solution_two()}")
