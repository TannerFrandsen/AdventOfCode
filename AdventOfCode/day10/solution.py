# Advent of Code day 10
# Author: Tanner Frandsen
# Date: 2020-12-10
import os
import sys


def load_puzzle_data(file):
    with open(file, 'r') as file_handle:
        data = file_handle.readlines()
        data = [int(line.strip()) for line in data]
        return data


def count_jolt_differences(puzzle_data, wall_jolts, device_jolts):
    addapter_list = list(puzzle_data).copy()
    addapter_list.append(wall_jolts)
    addapter_list.append(device_jolts)
    addapter_list = sorted(addapter_list)
    deltas = []
    for idx in range(1, len(addapter_list)):
        deltas.append(addapter_list[idx] - addapter_list[idx - 1])

    return deltas


def count_valid_adapter_configurations(puzzle_data):
    puzzle_input = puzzle_data.copy()
    puzzle_input.append(0)
    puzzle_input.append(max(puzzle_input) + 3)
    puzzle_input = sorted(puzzle_input)

    data = {adt: 0 for adt in puzzle_input}
    data[0] = 1

    for x in sorted(puzzle_input)[1:]:
        xm1 = data[x - 1] if x-1 in puzzle_input else 0
        xm2 = data[x - 2] if x-2 in puzzle_input else 0
        xm3 = data[x - 3] if x-3 in puzzle_input else 0
        data[x] = xm1 + xm2 + xm3

    return data[max(puzzle_input)]


def main(input_path):
    puzzle_input = load_puzzle_data(input_path)

    addapter_deltas = count_jolt_differences(puzzle_input, 0, max(puzzle_input) + 3)
    print(f'The solution to part 1 is {addapter_deltas.count(3) * addapter_deltas.count(1)}')

    valid_path_counts = count_valid_adapter_configurations(puzzle_input)
    print(f'The solution to part 2 is {valid_path_counts}')


if __name__ == '__main__':
    main(f'{os.path.join(sys.path[0])}\\example_input2.dat')
    main(f'{os.path.join(sys.path[0])}\\example_input.dat')
    main(f'{os.path.join(sys.path[0])}\\puzzle_input.dat')
