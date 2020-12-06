#!/usr/bin/env python3

filename = 'inputs/input2.txt'
nums = list()

with open(filename, 'r') as fin:
    lines = fin.read().split('\n')

# part 1
valid_count = 0
for line in lines:
    r, l, password = line.split(' ')
    low, high = (int(a) for a in r.split('-'))
    letter = l[0]

    count = password.count(letter)
    if count >= low and count <= high:
        valid_count += 1
print(f'Part 1: {valid_count}')

# part 2
valid_count = 0
for line in lines:
    r, l, password = line.split(' ')
    pos1, pos2 = (int(a)-1 for a in r.split('-'))
    letter = l[0]

    if (password[pos1] == letter) != (password[pos2] == letter):
        valid_count += 1
print(f'Part 2: {valid_count}')