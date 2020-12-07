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


def init_seat_map():
    seat_map = dict()
    i = 0
    j = 0
    while i < 128:
        while j < 8:
            seat_map[i * 8 + j] = 1
            j += 1
        j = 0
        i += 1
    return seat_map


def get_largest_sid(codes):
    largest_sid = 0
    seat_map = init_seat_map()
    for code in codes:
        seat = get_seat_id(code)
        del seat_map[seat]
        largest_sid = max(largest_sid, get_seat_id(code))
    return largest_sid, seat_map


def get_my_seat_id(seat_map):
    my_sid = -1
    for sid in seat_map.keys():
        if sid != my_sid + 1:
            my_sid = sid
            break
        my_sid = sid
    return my_sid


if __name__ == '__main__':
    with open(filename, 'r') as fin:
        lines = fin.read().split('\n')

    # part 1
    largest_sid, seat_map = get_largest_sid(lines)
    print(f'Largest seat ID: {largest_sid}')

    # part 2
    my_sid = get_my_seat_id(seat_map)
    print(f'My seat ID: {my_sid}')