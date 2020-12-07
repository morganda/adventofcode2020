#!/usr/bin/env python3


filename = 'inputs/input6.txt'


def count_yeses(submissions):
    sum = 0

    # part 1
    yes_lookup = set()
    for submission in submissions:
        if len(submission.strip()):
            for i in submission:
                yes_lookup.add(i)
        else:
            sum += len(yes_lookup)
            yes_lookup = set()

    # add last grouping
    sum += len(yes_lookup)

    return sum


def count_yeses_part2(submissions):
    sum = 0
    people_count = 0
    yes_lookup = dict()

    for submission in submissions:
        if len(submission.strip()):
            people_count += 1
            for i in submission:
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

    # add last grouping
    for _, count in yes_lookup.items():
        if count == people_count:
            sum += 1

    return sum


if __name__ == '__main__':
    with open(filename, 'r') as fin:
        lines = fin.read().split('\n')

    sum = count_yeses(lines)
    print(f'Sum of Counts: {sum}')

    # part 2
    sum = count_yeses_part2(lines)
    print(f'Sum of Counts Part 2: {sum}')