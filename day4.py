#!/usr/bin/env python3

import re

filename = 'inputs/input4.txt'
fields = ['byr', 'iyr', 'hgt', 'eyr',
        'hcl', 'ecl', 'pid']


def is_valid_birth_year(year):
    try:
        year = int(year)
        return year >= 1920 and year <= 2002
    except ValueError:
        return False


def is_valid_issue_year(year):
    try:
        year = int(year)
        return year >= 2010 and year <= 2020
    except ValueError:
        return False


def is_valid_expiration_year(year):
    try:
        year = int(year)
        return year >= 2020 and year <= 2030
    except ValueError:
        return False


def is_valid_height(hgt):
    try:
        measure = hgt[-2:]
        height = int(hgt[:-2])
        if measure == 'cm':
            return height >= 150 and height <= 193
        elif measure == 'in':
            return height >= 59 and height <= 76
        else:
            return False
    except ValueError:
        return False


def is_valid_hair_color(color):
    hair_color_pattern = re.compile('^#[a-z0-9]+$')
    return hair_color_pattern.match(color) is not None


def is_valid_eye_color(color):
    colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return color in colors


def is_valid_passport_id(pid):
    pid_pattern = re.compile('^(\d){9}$')
    return pid_pattern.match(pid) is not None


def is_valid_passport(passport):

    for field in fields:
        if field not in passport:
            return False
    return True


def is_valid_passport_p2(passport):
    try:
        return is_valid_birth_year(passport['byr']) and \
            is_valid_issue_year(passport['iyr']) and \
            is_valid_expiration_year(passport['eyr']) and \
            is_valid_height(passport['hgt']) and \
            is_valid_hair_color(passport['hcl']) and \
            is_valid_eye_color(passport['ecl']) and \
            is_valid_passport_id(passport['pid'])
    except KeyError:
        return False


if __name__ == '__main__':
    with open(filename, 'r') as fin:
        lines = fin.read().split('\n')
    
    valid_passports = 0
    valid_passports_p2 = 0
    passport = dict()

    for line in lines:
        if len(line.strip()):
            for attr in line.split(' '):
                attr, val = attr.split(':')
                passport[attr] = val
        else:
            if is_valid_passport(passport):
                valid_passports += 1
            if is_valid_passport_p2(passport):
                valid_passports_p2 += 1
            passport = dict()
    print(f'Valid Passports: {valid_passports}')
    print(f'Valid Passports Part 2: {valid_passports_p2}')