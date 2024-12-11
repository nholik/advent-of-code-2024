from collections import defaultdict
import heapq

left_nums, right_nums = [], []

right_side_counts = defaultdict(int)

with open("./data/1/input.txt", "r", encoding="utf-8") as f:
    for line in f:
        num_1, num_2 = line.split("  ")
        left_nums.append(int(num_1))

        r = int(num_2)
        right_side_counts[r] += 1
        right_nums.append(r)

heapq.heapify(left_nums)
heapq.heapify(right_nums)

result_part_one = 0
result_part_two = 0

while left_nums:
    l = heapq.heappop(left_nums)
    r = heapq.heappop(right_nums)
    result_part_one += abs(l - r)
    result_part_two += right_side_counts[l] * l

print(f"Part one: {result_part_one}")
print(f"Part two: {result_part_two}")
