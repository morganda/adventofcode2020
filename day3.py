#!/usr/bin/env python3

filename = 'inputs/input3.txt'

def traverse(lines, slope_x, slope_y):
    x, y = (0,0)
    trees = 0
    while y < len(lines):
        if lines[y][x] == '#':
            #print(f'Tree: {x}, {y}')
            trees += 1
        x = (x + slope_x) % len(lines[y])
        y += slope_y
    print(f'Trees with slope {slope_x}, {slope_y}: {trees}')
    return trees

if __name__ == '__main__':
    with open(filename, 'r') as fin:
        terrain = fin.read().split()
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]
    product = 1
    for slope in slopes:
        product *= traverse(terrain, slope[0], slope[1])
    print(f'Tree Product: {product}')
