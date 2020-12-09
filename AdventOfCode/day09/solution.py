# Advent of Code day 09
# Author: Tanner Frandsen
# Date: 2020-12-09


import itertools


def load_puzzle_data(file):
    with open(file, 'r') as file_handle:
        file_data = file_handle.readlines()
    return [int(line.strip()) for line in file_data]


def find_key_number(data, preamble_length):
    for target_idx, target in enumerate(data[preamble_length:], preamble_length):
        preamble = data[target_idx - preamble_length: target_idx]
        valid = False
        for num1, num2 in itertools.combinations(preamble, 2):
            if num1 == num2:
                continue

            if num1 + num2 == target:
                valid = True
                break

        if not valid:
            return target


def find_contiguous_range_extents(data, target):
    for base_idx in range(0, len(data)):
        for runner in range(base_idx + 1, len(data)):
            range_sum = sum(data[base_idx: runner])
            if range_sum == target:
                return min(data[base_idx: runner]), max(data[base_idx: runner])
            elif range_sum > target:
                break


def main(input_path):
    puzzle_data = load_puzzle_data(input_path)
    key_number = find_key_number(puzzle_data, 25)
    print(key_number)
    min, max = find_contiguous_range_extents(puzzle_data, key_number)
    print(min + max)


if __name__ == '__main__':
    main(r'../input/day_09.txt')
