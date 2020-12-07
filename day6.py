#!/usr/bin/env python3


filename = 'inputs/input6.txt'


if __name__ == '__main__':
    with open(filename, 'r') as fin:
        lines = fin.read().split('\n')

    sum = 0

    # part 1
    yes_lookup = set()
    for line in lines:
        if len(line.strip()):
            for i in line:
                yes_lookup.add(i)
        else:
            sum += len(yes_lookup)
            yes_lookup = set()
    sum += len(yes_lookup)

    print(f'Sum of Counts: {sum}')

    # part 2
    sum = 0
    people_count = 0
    yes_lookup = dict()

    for line in lines:
        if len(line.strip()):
            people_count += 1
            for i in line:
                if i not in yes_lookup:
                    yes_lookup[i] = 1
                else:
                    yes_lookup[i] +=1
        else:
            for _, count in yes_lookup.items():
                if count == people_count:
                    sum += 1
            people_count = 0
            yes_lookup = dict()

    for _, count in yes_lookup.items():
        if count == people_count:
            sum += 1

    print(f'Sum of Counts Part 2: {sum}')