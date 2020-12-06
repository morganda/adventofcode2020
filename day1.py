#!/usr/bin/env python3

filename = 'inputs/input.txt'
nums = dict()

with open(filename, 'r') as fin:
    lines = fin.read().split()

for line in lines:
    num = int(line)
    if num in nums:
        nums[num] += 1
    else:
        nums[num] = 1

for num in nums:
    diff = 2020 - num
    if diff in nums or nums[num] > 1:
        print(diff * num)
        break


print('finished looking')