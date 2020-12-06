#!/usr/bin/env python3

filename = 'inputs/input.txt'
nums = list()

with open(filename, 'r') as fin:
    lines = fin.read().split()

for line in lines:
    num = int(line)
    nums.append(num)

partials = dict()
for i in range(len(nums) - 1):
    j = i + 1
    while j < len(nums):
        partial = abs(nums[j] + nums[i])
        if partial < 2020:
            partials[partial] = (nums[j], nums[i])
        j += 1

num_lookup = map(1, nums)
for partial in partials:
    diff = 2020 - partial
    if diff in nums:
        a, b = partials[partial]
        print(f'{diff} {a} {b}')
        print(diff * a * b)
        break


print('finished looking')