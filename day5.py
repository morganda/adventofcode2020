#!/usr/bin/env python3

import math

filename = 'inputs/input5.txt'


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


def get_seat_id_fast(code):
    row_code = code[:7]
    col_code = code[7:]

    row_bin = ''.join(['0' if i == 'F' else '1' for i in row_code])
    row = int(row_bin, 2)
    col_bin = ''.join(['0' if i == 'L' else '1' for i in col_code])
    col = int(col_bin, 2)

    sid = row * 8 + col
    return sid


def get_largest_sid(codes):
    largest_sid = 0
    seat_map = init_seat_map()
    for code in codes:
        seat = get_seat_id_fast(code)
        del seat_map[seat]
        largest_sid = max(largest_sid, seat)
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