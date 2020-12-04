# Advent of Code day 04
# Author: Tanner Frandsen
# Date: 2020-12-04

import re


def load_puzzle_data(file):
    with open(file, 'r') as file_handle:
        file_data = file_handle.read()
    passports_strings = file_data.split('\n\n')
    passports_strings = [passport_string.replace('\n', ' ') for passport_string in passports_strings]

    passports = []
    for passport_string in passports_strings:
        passport = {}
        for field in passport_string.split(' '):
            key, value = field.split(':')
            passport[key] = value
        passports.append(passport)
    return passports


def valid_passport(passport, passport_requirements):
    for field, validator, arguments in passport_requirements:
        if not validator(passport[field], **arguments):
            return False
    return True


def count_valid_passports(passports, passport_requirements):
    valid_count = 0
    invalid_count = 0
    required_fields = [field for field, *_ in passport_requirements]
    for passport in passports:
        # Is missing fields
        if not all(field in passport.keys() for field in required_fields):
            invalid_count = invalid_count + 1

        else:
            if valid_passport(passport, passport_requirements):
                valid_count = valid_count + 1
            else:
                invalid_count = invalid_count + 1

    return valid_count


def number_validator(field, min_range, max_range):
    return int(field) in range(min_range, max_range+1)


def heigth_validator(field, kwargs={}):
    if not re.match(r'(\d+) *(in|cm)', field):
        return False

    number, unit = re.match(r'(\d+) *(in|cm)', field).groups()
    if unit == 'cm':
        return number_validator(number, 150, 193)
    elif unit == 'in':
        return number_validator(number, 59, 76)
    else:
        return False


def string_validator(field, regex_rule):
    return re.match(regex_rule, field)


def no_validator(field, kwargs={}):
    return True


def main(input_path):
    passports = load_puzzle_data(input_path)

    passport_requirements = [
        ('byr', no_validator, {}),
        ('iyr', no_validator, {}),
        ('eyr', no_validator, {}),
        ('hgt', no_validator, {}),
        ('hcl', no_validator, {}),
        ('ecl', no_validator, {}),
        ('pid', no_validator, {})]
    valid_passport_count = count_valid_passports(passports, passport_requirements)
    print(f'Valid passport count {valid_passport_count}')

    passport_requirements = [
        ('byr', number_validator, {'min_range': 1920, 'max_range': 2002}),
        ('iyr', number_validator, {'min_range': 2010, 'max_range': 2020}),
        ('eyr', number_validator, {'min_range': 2020, 'max_range': 2030}),
        ('hgt', heigth_validator, {}),
        ('hcl', string_validator, {'regex_rule': r'^#[0-9a-f]{6}$'}),
        ('ecl', string_validator, {'regex_rule': r'^amb|blu|brn|gry|grn|hzl|oth$'}),
        ('pid', string_validator, {'regex_rule': r'^\d{9}$'})]
    strict_valid_passport_count = count_valid_passports(passports, passport_requirements)
    print(f'Strict valid passport count {strict_valid_passport_count}')


if __name__ == '__main__':
    main(r'..\prompts\day_04_input.txt')
