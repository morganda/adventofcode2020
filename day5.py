#!/usr/bin/env python3

import math

filename = 'inputs/input5.txt'

def get_seat_id(code):
    low = 0
    high = 127
    i = 0
    while i < 7:
        mid = (low + high) / 2
        if code[i] == 'F':
            high = math.floor(mid)
        else:
            low = math.ceil(mid)
        i += 1

    row = low

    low = 0
    high = 7
    while i < 10:
        mid = (low + high) / 2
        if code[i] == 'L':
            high = math.floor(mid)
        else:
            low = math.ceil(mid)
        i += 1

    col = low

    sid = row * 8 + col
    #print(f'row: {row}, col: {col}, sid: {sid}')
    return sid


if __name__ == '__main__':
    with open(filename, 'r') as fin:
        lines = fin.read().split('\n')

    # seat map for part 2
    seat_map = dict()
    i = 0
    j = 0
    while i < 128:
        while j < 8:
            seat_map[i * 8 + j] = 1
            j += 1
        j = 0
        i += 1

    largest_sid = 0
    for line in lines:
        seat = get_seat_id(line)
        del seat_map[seat]
        largest_sid = max(largest_sid, get_seat_id(line))  # part 1

    my_sid = -1
    for sid in seat_map.keys():
        if sid != my_sid + 1:
            my_sid = sid
            break
        my_sid = sid

    print(f'Largest seat ID: {largest_sid}')
    print(f'My seat ID: {my_sid}')